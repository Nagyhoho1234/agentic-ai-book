"""Semantic response cache backed by SQLite."""

import hashlib
from typing import Optional

import numpy as np
import structlog

from backend.config import settings
from backend.db.database import get_db

logger = structlog.get_logger()


class ResponseCache:
    """Cache LLM responses with exact-match hash lookup.

    For semantic similarity matching, we use the embedding model
    to compare prompts. For fast lookup, we also store a hash.
    """

    def __init__(self) -> None:
        self._embedder = None

    def _get_embedder(self):
        """Lazy-load the embedding model."""
        if self._embedder is None:
            from sentence_transformers import SentenceTransformer
            self._embedder = SentenceTransformer(settings.embedding_model)
        return self._embedder

    @staticmethod
    def _hash_prompt(prompt: str) -> str:
        return hashlib.sha256(prompt.strip().lower().encode()).hexdigest()

    def _embed(self, text: str) -> np.ndarray:
        return self._get_embedder().encode(text, normalize_embeddings=True)

    @staticmethod
    def _cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
        return float(np.dot(a, b))

    async def get(self, prompt: str) -> Optional[str]:
        """Look up a cached response. Returns None on miss."""
        prompt_hash = self._hash_prompt(prompt)

        db = await get_db()
        try:
            # Fast path: exact hash match
            cursor = await db.execute(
                "SELECT id, response_text FROM response_cache WHERE prompt_hash = ?",
                (prompt_hash,),
            )
            row = await cursor.fetchone()
            if row:
                await db.execute(
                    "UPDATE response_cache SET last_accessed = CURRENT_TIMESTAMP, access_count = access_count + 1 WHERE id = ?",
                    (row[0],),
                )
                await db.commit()
                await logger.ainfo("cache_hit", method="exact_hash")
                return row[1]

            # Slow path: semantic similarity over recent entries
            cursor = await db.execute(
                "SELECT id, prompt_text, response_text FROM response_cache ORDER BY last_accessed DESC LIMIT 500"
            )
            rows = await cursor.fetchall()

            if rows:
                query_emb = self._embed(prompt)
                best_score = 0.0
                best_response = None
                best_id = None

                for row in rows:
                    candidate_emb = self._embed(row[1])
                    score = self._cosine_sim(query_emb, candidate_emb)
                    if score > best_score:
                        best_score = score
                        best_response = row[2]
                        best_id = row[0]

                if best_score >= settings.cache_similarity_threshold and best_id is not None:
                    await db.execute(
                        "UPDATE response_cache SET last_accessed = CURRENT_TIMESTAMP, access_count = access_count + 1 WHERE id = ?",
                        (best_id,),
                    )
                    await db.commit()
                    await logger.ainfo("cache_hit", method="semantic", similarity=round(best_score, 3))
                    return best_response

            return None
        finally:
            await db.close()

    async def put(self, prompt: str, response: str, model_used: str = "") -> None:
        """Store a response in the cache."""
        prompt_hash = self._hash_prompt(prompt)

        db = await get_db()
        try:
            # Evict oldest entries if at capacity
            cursor = await db.execute("SELECT COUNT(*) FROM response_cache")
            count_row = await cursor.fetchone()
            if count_row and count_row[0] >= settings.cache_max_entries:
                await db.execute(
                    "DELETE FROM response_cache WHERE id IN (SELECT id FROM response_cache ORDER BY last_accessed ASC LIMIT 100)"
                )

            await db.execute(
                "INSERT INTO response_cache (prompt_hash, prompt_text, response_text, model_used) VALUES (?, ?, ?, ?)",
                (prompt_hash, prompt, response, model_used),
            )
            await db.commit()
            await logger.ainfo("cache_store", model=model_used)
        finally:
            await db.close()

    async def get_stats(self) -> dict:
        """Return cache statistics."""
        db = await get_db()
        try:
            cursor = await db.execute("SELECT COUNT(*), SUM(access_count) FROM response_cache")
            row = await cursor.fetchone()
            return {
                "entries": row[0] if row else 0,
                "total_hits": row[1] if row and row[1] else 0,
                "max_entries": settings.cache_max_entries,
            }
        finally:
            await db.close()


# Singleton
response_cache = ResponseCache()
