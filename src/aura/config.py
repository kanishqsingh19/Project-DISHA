"""
AURA Configuration

Loads environment-based configuration for Project DISHA.
"""

import os


class AURAConfig:
    """Central configuration for AURA."""

    def __init__(self):
        # Gemini
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")

        # Generic cloud configuration
        self.cloud_api_key = os.getenv("CLOUD_AI_API_KEY")
        self.cloud_endpoint = os.getenv("CLOUD_AI_ENDPOINT")

        # Local AI
        self.local_endpoint = os.getenv("LOCAL_AI_ENDPOINT")

        # Specialized AI
        self.specialized_api_key = os.getenv(
            "SPECIALIZED_AI_API_KEY"
        )

        # Application
        self.environment = os.getenv(
            "AURA_ENVIRONMENT",
            "development"
        )

    def gemini_configured(self):
        """Check whether Gemini is configured."""
        return bool(self.gemini_api_key)

    def cloud_configured(self):
        """Check whether generic cloud AI is configured."""
        return bool(
            self.cloud_api_key
            and self.cloud_endpoint
        )

    def local_configured(self):
        """Check whether local AI is configured."""
        return bool(self.local_endpoint)

    def specialized_configured(self):
        """Check whether specialized AI is configured."""
        return bool(self.specialized_api_key)
