"""
AURA AI Provider Interface

Defines the common interface that all AI providers
must follow.
"""


class AIProvider:
    """Base interface for an AURA AI provider."""

    def generate(self, messages):
        """
        Generate a response from the AI provider.

        Individual providers will implement this method.
        """
        raise NotImplementedError(
            "AI providers must implement the generate method."
        )
