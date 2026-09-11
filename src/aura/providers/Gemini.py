"""
AURA Gemini Provider

Google Gemini cloud AI provider adapter.
"""

from .cloud import CloudAIProvider
from ..config import AURAConfig


class GeminiProvider(CloudAIProvider):
    """Cloud provider adapter for Google Gemini."""

    provider_name = "gemini"

    def __init__(self):
        self.config = AURAConfig()

    def is_configured(self):
        """Check whether Gemini is configured."""
        return self.config.gemini_configured()

    def generate(self, messages):
        """Generate a response using Google Gemini."""

        if not messages:
            return {
                "status": "error",
                "message": "No messages were provided."
            }

        if not self.is_configured():
            return {
                "status": "not_configured",
                "message": "Gemini provider is not configured."
            }

        return {
            "status": "pending",
            "message": "Gemini integration is not implemented yet."
        }
