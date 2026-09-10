"""
AURA Provider Status

Checks the availability of AURA's AI providers.
"""

from .local import LocalAIProvider
from .cloud import CloudAIProvider
from .specialized import SpecializedAIProvider


class ProviderStatus:
    """Reports the configuration status of AI providers."""

    def __init__(self):
        self.providers = {
            "local": LocalAIProvider(),
            "cloud": CloudAIProvider(),
            "specialized": SpecializedAIProvider()
        }

    def check(self):
        """Return the configuration status of each provider."""

        return {
            "local": self.providers["local"].is_configured(),
            "cloud": self.providers["cloud"].is_configured(),
            "specialized": self.providers["specialized"].is_configured()
        }
