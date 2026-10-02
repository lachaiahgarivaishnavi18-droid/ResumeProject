from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class LLMService:
    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini"):
        self.api_key = api_key or ""
        self.model = model

    def generate(self, prompt: str, **kwargs: Any) -> str:
        if not self.api_key:
            logger.warning("No OpenAI API key configured. Returning a fallback response.")
            return "This is a mock LLM response because no API key is configured."
        return f"LLM output generated for model={self.model}: {prompt[:200]}"

    def embed(self, text: str) -> list[float]:
        if not self.api_key:
            return [0.0] * 1536
        return [0.0] * 1536
