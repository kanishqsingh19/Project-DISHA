"""
AURA Groq Provider

Groq cloud AI provider adapter.
"""

from .cloud import CloudAIProvider
from ..config import AURAConfig


class GroqProvider(CloudAIProvider):
    """Cloud provider adapter for Groq."""

    provider_name = "groq"

    def __init__(self):
        self.config = AURAConfig()

    def is_configured(self):
        """Check whether Groq is configured."""
        return self.config.groq_configured()

    def generate(self, messages):
        """Generate a response using Groq."""

        if not messages:
            return {
                "status": "error",
                "message": "No messages were provided."
            }

        if not self.is_configured():
            return {
                "status": "not_configured",
                "message": "Groq provider is not configured."
            }

        return {
            "status": "pending",
            "message": "Groq integration is not implemented yet."
        }
