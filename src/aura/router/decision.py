"""
AURA Routing Decision

Provides the foundation for intelligent provider selection.
"""


class RoutingDecision:
    """Makes routing decisions for AURA."""

    def __init__(self):
        self.providers = [
            "local",
            "cloud",
            "specialized"
        ]

    def choose(self, available_providers):
        """Choose the first available provider."""

        for provider in self.providers:
            if provider in available_providers:
                return provider

        return None
