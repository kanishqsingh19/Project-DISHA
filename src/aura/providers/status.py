"""
AURA Provider Status

Checks the availability of AURA's AI providers.
"""


class ProviderStatus:
    """Reports the configuration status of registered AI providers."""

    def __init__(self, registry):
        self.registry = registry

    def check(self):
        """Return the configuration status of all registered providers."""

        return {
            provider_name: provider_name
            in self.registry.available_providers()
            for provider_name in self.registry.list_providers()
        }
