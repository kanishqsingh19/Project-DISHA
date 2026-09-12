"""
AURA Provider Status

Checks the availability of AURA's AI providers.
"""

from .local import LocalAIProvider
from .gemini import GeminiProvider
from .specialized import SpecializedAIProvider


class ProviderStatus:
    """Reports the configuration status of AI providers."""

    def __init__(self):
        self.providers = {
            "local": LocalAIProvider(),
            "gemini": GeminiProvider(),
            "specialized": SpecializedAIProvider()
        }

    def check(self):
        """Return the configuration status of each AI provider."""

        return {
            provider_name: provider.is_configured()
            for provider_name, provider in self.providers.items()
        }
