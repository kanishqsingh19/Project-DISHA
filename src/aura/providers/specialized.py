"""
AURA Specialized AI Provider

Placeholder for future specialized AI integrations.
"""

from .base import AIProvider


class SpecializedAIProvider(AIProvider):
    """AI provider for specialized AI capabilities."""

    def generate(self, messages):
        """Generate a response using specialized AI."""
        raise NotImplementedError(
            "Specialized AI integration is not implemented yet."
        )
