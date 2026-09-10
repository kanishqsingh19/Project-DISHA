"""
AURA Response Model

Defines a standard response structure for AURA.
"""


class AURAResponse:
    """Standard response returned by AURA."""

    def __init__(
        self,
        content="",
        status="success",
        provider=None
    ):
        self.content = content
        self.status = status
        self.provider = provider

    def to_dict(self):
        """Convert the response into a dictionary."""
        return {
            "content": self.content,
            "status": self.status,
            "provider": self.provider
        }
