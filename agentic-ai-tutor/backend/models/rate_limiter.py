"""Rate limiter for Gemini API calls — token bucket + daily counter."""

import time
import asyncio
from datetime import datetime, timezone
from typing import Optional

import aiosqlite
import structlog

from backend.config import settings
from backend.db.database import get_db

logger = structlog.get_logger()


class RateLimiter:
    """Per-model rate limiting with RPM (token bucket) and RPD (daily counter)."""

    def __init__(self) -> None:
        # Model configs: (rpm_limit, rpd_limit)
        self.limits: dict[str, tuple[int, int]] = {
            settings.model_flash_lite: (settings.rpm_flash_lite, settings.rpd_flash_lite),
            settings.model_flash: (settings.rpm_flash, settings.rpd_flash),
            settings.model_pro: (settings.rpm_pro, settings.rpd_pro),
        }

        # Token buckets for RPM: {model: (tokens_available, last_refill_time)}
        self._buckets: dict[str, tuple[float, float]] = {}
        for model, (rpm, _) in self.limits.items():
            self._buckets[model] = (float(rpm), time.monotonic())

        self._lock = asyncio.Lock()

    def _today_str(self) -> str:
        """Current date string in PT timezone for daily reset."""
        # Use UTC-8 as approximation for Pacific Time
        from datetime import timedelta
        pt_now = datetime.now(timezone.utc) - timedelta(hours=8)
        return pt_now.strftime("%Y-%m-%d")

    def _refill_bucket(self, model: str) -> float:
        """Refill token bucket based on elapsed time. Returns available tokens."""
        rpm_limit = self.limits[model][0]
        tokens, last_time = self._buckets[model]
        now = time.monotonic()
        elapsed = now - last_time
        # Refill rate: rpm_limit tokens per 60 seconds
        new_tokens = min(float(rpm_limit), tokens + elapsed * (rpm_limit / 60.0))
        self._buckets[model] = (new_tokens, now)
        return new_tokens

    async def _get_daily_count(self, model: str) -> int:
        """Get today's request count from SQLite."""
        db = await get_db()
        try:
            cursor = await db.execute(
                "SELECT request_count FROM rate_limits WHERE model = ? AND date = ?",
                (model, self._today_str()),
            )
            row = await cursor.fetchone()
            return row[0] if row else 0
        finally:
            await db.close()

    async def can_request(self, model: str) -> bool:
        """Check if a request can be made to the given model."""
        if model not in self.limits:
            return False

        async with self._lock:
            # Check RPM (token bucket)
            available = self._refill_bucket(model)
            if available < 1.0:
                return False

            # Check RPD (daily counter)
            _, rpd_limit = self.limits[model]
            daily_count = await self._get_daily_count(model)
            if daily_count >= rpd_limit:
                return False

            return True

    async def record_request(self, model: str) -> None:
        """Record that a request was made to the given model."""
        async with self._lock:
            # Consume one RPM token
            tokens, last_time = self._buckets[model]
            self._buckets[model] = (max(0.0, tokens - 1.0), last_time)

            # Increment daily counter
            today = self._today_str()
            db = await get_db()
            try:
                await db.execute(
                    """INSERT INTO rate_limits (model, date, request_count)
                       VALUES (?, ?, 1)
                       ON CONFLICT(model, date) DO UPDATE SET request_count = request_count + 1""",
                    (model, today),
                )
                await db.commit()
            finally:
                await db.close()

        await logger.ainfo("api_request_recorded", model=model)

    async def get_quota_status(self) -> dict:
        """Return current quota status for all models."""
        status = {}
        for model, (rpm_limit, rpd_limit) in self.limits.items():
            daily_count = await self._get_daily_count(model)
            available_rpm = self._refill_bucket(model)
            status[model] = {
                "rpm_limit": rpm_limit,
                "rpm_available": round(available_rpm, 1),
                "rpd_limit": rpd_limit,
                "rpd_used": daily_count,
                "rpd_remaining": max(0, rpd_limit - daily_count),
                "exhausted": daily_count >= rpd_limit,
            }
        return status

    async def get_best_available_model(self, preferred: str) -> Optional[str]:
        """Get the best available model, falling back to lower tiers."""
        # Priority order based on preferred model
        fallback_chains = {
            settings.model_pro: [settings.model_pro, settings.model_flash, settings.model_flash_lite],
            settings.model_flash: [settings.model_flash, settings.model_flash_lite],
            settings.model_flash_lite: [settings.model_flash_lite],
        }
        chain = fallback_chains.get(preferred, [settings.model_flash_lite])
        for model in chain:
            if await self.can_request(model):
                return model
        return None


# Singleton
rate_limiter = RateLimiter()
