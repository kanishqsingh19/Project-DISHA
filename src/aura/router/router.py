"""
AURA Intelligence Router

Routes user requests to the appropriate AI provider.
"""

from ..providers.local import LocalAIProvider
from ..providers.cloud import CloudAIProvider
from ..providers.specialized import SpecializedAIProvider


class IntelligenceRouter:
    """Central routing layer for AURA's hybrid AI architecture."""

    def __init__(self):
        self.providers = {
            "local": LocalAIProvider(),
            "cloud": CloudAIProvider(),
            "specialized": SpecializedAIProvider()
        }

    def get_provider(self, provider_name):
        """Return a registered AI provider."""
        return self.providers.get(provider_name)

    def route(self, request, provider_name="cloud"):
        """
        Route a request to the selected provider.

        Actual provider selection logic will be added later.
        """
        provider = self.get_provider(provider_name)

        if provider is None:
            return {
                "status": "error",
                "message": "Requested AI provider is unavailable."
            }

        return {
            "status": "ready",
            "request": request,
            "provider": provider_name
        }
