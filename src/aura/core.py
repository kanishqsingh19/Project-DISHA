"""
AURA Core

Central orchestration layer for the AURA assistant.
"""

from .conversation.engine import ConversationEngine
from .router.router import IntelligenceRouter
from .security.permissions import PermissionManager
from .skills.manager import SkillManager


class AURACore:
    """Central coordinator for AURA."""

    def __init__(self):
        self.conversation = ConversationEngine()
        self.router = IntelligenceRouter()
        self.permissions = PermissionManager()
        self.skills = SkillManager()

    def process(self, request):
        """Process a user request through the AURA foundation."""
        self.conversation.add_message("user", request)

        return {
            "status": "received",
            "request": request
        }
