"""
AURA Configuration

Loads environment-based configuration for Project DISHA.
"""

import os


class AURAConfig:
    """Central configuration for AURA."""

    def __init__(self):
        self.cloud_api_key = os.getenv("CLOUD_AI_API_KEY")
        self.cloud_endpoint = os.getenv("CLOUD_AI_ENDPOINT")

        self.local_endpoint = os.getenv("LOCAL_AI_ENDPOINT")

        self.specialized_api_key = os.getenv(
            "SPECIALIZED_AI_API_KEY"
        )

        self.environment = os.getenv(
            "AURA_ENVIRONMENT",
            "development"
        )

    def cloud_configured(self):
        """Check whether cloud AI configuration is available."""
        return bool(
            self.cloud_api_key
            and self.cloud_endpoint
        )

    def local_configured(self):
        """Check whether local AI configuration is available."""
        return bool(self.local_endpoint)

    def specialized_configured(self):
        """Check whether specialized AI configuration is available."""
        return bool(self.specialized_api_key)
