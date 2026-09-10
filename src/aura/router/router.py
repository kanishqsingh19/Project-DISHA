"""
AURA Intelligence Router

Routes user requests to the appropriate AI provider.
"""

from ..config import AURAConfig
from ..providers.local import LocalAIProvider
from ..providers.cloud import CloudAIProvider
from ..providers.specialized import SpecializedAIProvider
from ..providers.status import ProviderStatus


class IntelligenceRouter:
    """Central routing layer for AURA's hybrid AI architecture."""

    def __init__(self):
        self.config = AURAConfig()
        self.status = ProviderStatus()

        self.providers = {
            "local": LocalAIProvider(),
            "cloud": CloudAIProvider(),
            "specialized": SpecializedAIProvider()
        }

    def get_provider(self, provider_name):
        """Return a registered AI provider."""
        return self.providers.get(provider_name)

    def get_status(self):
        """Return the availability of all AI providers."""
        return self.status.check()

    def route(self, request, provider_name="cloud"):
        """
        Route a request to the selected provider.

        Automatic provider selection will be added later.
        """

        provider = self.get_provider(provider_name)

        if provider is None:
            return {
                "status": "error",
                "message": "Requested AI provider is unavailable."
            }

        if not provider.is_configured():
            return {
                "status": "not_configured",
                "request": request,
                "provider": provider_name
            }

        return {
            "status": "ready",
            "request": request,
            "provider": provider_name,
            "environment": self.config.environment
        }
