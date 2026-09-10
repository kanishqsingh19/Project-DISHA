"""
AURA Cloud AI Provider

Placeholder for future cloud AI integrations.
"""

from .base import AIProvider


class CloudAIProvider(AIProvider):
    """AI provider for cloud-based AI services."""

    def generate(self, messages):
        """Generate a response using cloud AI."""
        raise NotImplementedError(
            "Cloud AI integration is not implemented yet."
        )
