"""
AURA Local AI Provider

Placeholder for future local AI integration.
"""

from .base import AIProvider


class LocalAIProvider(AIProvider):
    """AI provider for locally running models."""

    def generate(self, messages):
        """Generate a response using local AI."""
        raise NotImplementedError(
            "Local AI integration is not implemented yet."
        )
