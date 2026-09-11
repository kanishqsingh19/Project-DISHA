"""
AURA Cloud Provider Base

Common foundation for cloud-based AI providers.
"""

from .base import AIProvider


class CloudAIProvider(AIProvider):
    """Base interface for cloud AI providers."""

    provider_name = "cloud"

    def is_configured(self):
        """Check whether this cloud provider is configured."""
        raise NotImplementedError(
            "Cloud providers must implement is_configured."
        )

    def generate(self, messages):
        """Generate a response from a cloud AI provider."""
        raise NotImplementedError(
            "Cloud providers must implement generate."
        )
