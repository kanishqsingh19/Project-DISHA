"""
AURA Provider Registry

Central registry for all AI providers used by AURA.
"""


class ProviderRegistry:
    """Registers and manages AURA AI providers."""

    def __init__(self):
        self.providers = {}

    def register(self, provider):
        """Register an AI provider."""

        provider_name = getattr(provider, "provider_name", None)

        if not provider_name:
            raise ValueError(
                "AI providers must define a provider_name."
            )

        self.providers[provider_name] = provider

    def get(self, provider_name):
        """Return a registered provider."""
        return self.providers.get(provider_name)

    def list_providers(self):
        """Return the names of all registered providers."""
        return list(self.providers.keys())

    def available_providers(self):
        """Return providers that are currently configured."""

        return [
            provider_name
            for provider_name, provider in self.providers.items()
            if provider.is_configured()
        ]
