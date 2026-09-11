"""
AURA Cloud AI Provider

Base implementation for future cloud AI integrations.
"""

from .base import AIProvider
from ..config import AURAConfig


class CloudAIProvider(AIProvider):
    """Base cloud AI provider."""

    def __init__(self):
        self.config = AURAConfig()

    def is_configured(self):
        """Check whether the cloud provider is configured."""
        return self.config.cloud_configured()

    def generate(self, messages):
        """
        Generate a response using a cloud AI service.

        Actual API communication will be implemented later.
        """
        
        if not messages:
            return {
                "status": "error",
                "message": "No messages were provided."
            }
            
        if not self.is_configured():
            return {
                "status": "not_configured",
                "message": "Cloud AI provider is not configured."
            }

        return {
            "status": "pending",
            "message": "Cloud AI integration is not implemented yet."
        }
