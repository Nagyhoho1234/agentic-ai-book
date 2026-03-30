"""Gemini API client with smart model routing and rate limiting."""

import asyncio
from dataclasses import dataclass
from typing import Optional

import google.generativeai as genai
import structlog

from backend.config import settings
from backend.models.rate_limiter import rate_limiter

logger = structlog.get_logger()


@dataclass
class LLMResponse:
    """Structured response from Gemini."""
    text: str
    model_used: str
    prompt_tokens: int
    response_tokens: int
    cached: bool = False


# Complexity -> preferred model mapping
COMPLEXITY_MODEL_MAP = {
    "low": settings.model_flash_lite,
    "medium": settings.model_flash,
    "high": settings.model_pro,
}


class GeminiClient:
    """Wraps the Gemini API with rate limiting and model routing."""

    def __init__(self) -> None:
        if settings.gemini_api_key:
            genai.configure(api_key=settings.gemini_api_key)
        self._models_cache: dict[str, genai.GenerativeModel] = {}

    def _get_model(self, model_name: str) -> genai.GenerativeModel:
        """Get or create a GenerativeModel instance."""
        if model_name not in self._models_cache:
            self._models_cache[model_name] = genai.GenerativeModel(model_name)
        return self._models_cache[model_name]

    async def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        complexity: str = "medium",
        max_retries: int = 3,
    ) -> Optional[LLMResponse]:
        """Generate a response with automatic model routing and retry."""

        preferred_model = COMPLEXITY_MODEL_MAP.get(complexity, settings.model_flash)
        model_name = await rate_limiter.get_best_available_model(preferred_model)

        if model_name is None:
            await logger.awarn("all_models_exhausted", complexity=complexity)
            return None

        for attempt in range(max_retries):
            try:
                model = self._get_model(model_name)

                # Build content
                contents = []
                if system_prompt:
                    contents.append({"role": "user", "parts": [system_prompt]})
                    contents.append({"role": "model", "parts": ["Understood. I will follow these instructions."]})
                contents.append({"role": "user", "parts": [prompt]})

                # Make the API call in a thread to not block the event loop
                response = await asyncio.to_thread(
                    model.generate_content, contents
                )

                # Record usage
                await rate_limiter.record_request(model_name)

                # Extract token counts
                prompt_tokens = getattr(response.usage_metadata, "prompt_token_count", 0) if hasattr(response, "usage_metadata") else 0
                response_tokens = getattr(response.usage_metadata, "candidates_token_count", 0) if hasattr(response, "usage_metadata") else 0

                result = LLMResponse(
                    text=response.text,
                    model_used=model_name,
                    prompt_tokens=prompt_tokens,
                    response_tokens=response_tokens,
                )

                await logger.ainfo(
                    "gemini_response",
                    model=model_name,
                    prompt_tokens=prompt_tokens,
                    response_tokens=response_tokens,
                )
                return result

            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "quota" in error_str.lower():
                    # Rate limited — try fallback model
                    await logger.awarn("rate_limited", model=model_name, attempt=attempt)
                    model_name = await rate_limiter.get_best_available_model(settings.model_flash_lite)
                    if model_name is None:
                        return None
                    # Exponential backoff
                    await asyncio.sleep(2 ** attempt)
                else:
                    await logger.aerror("gemini_error", error=error_str, model=model_name)
                    if attempt == max_retries - 1:
                        return None
                    await asyncio.sleep(1)

        return None


# Singleton
gemini_client = GeminiClient()
