"""
AURA Intelligence Router

Routes user requests to the appropriate AI provider.
"""

from ..config import AURAConfig
from ..providers.local import LocalAIProvider
from ..providers.gemini import GeminiProvider
from ..providers.specialized import SpecializedAIProvider
from ..providers.registry import ProviderRegistry
from ..providers.status import ProviderStatus
from .decision import RoutingDecision


class IntelligenceRouter:
    """Central routing layer for AURA's hybrid AI architecture."""

    def __init__(self):
        self.config = AURAConfig()
        self.decision = RoutingDecision()
        self.registry = ProviderRegistry()

        self.registry.register(LocalAIProvider())
        self.registry.register(GeminiProvider())
        self.registry.register(SpecializedAIProvider())

        self.status = ProviderStatus(self.registry)
        
    def get_provider(self, provider_name):
        """Return a registered AI provider."""
        return self.registry.get(provider_name)

    def get_status(self):
        """Return the availability of all registered providers."""
        
        return self.status.check()

    def select_provider(self, request):
        """Select the best available provider."""

        available_providers = self.registry.available_providers()

        return self.decision.choose(
            request,
            available_providers
        )

    def route(self, request, provider_name=None):
        """Route a request to the selected provider."""

        if provider_name is None:
            provider_name = self.select_provider(request)

        if provider_name is None:
            return {
                "status": "no_provider_available",
                "request": request
            }

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
