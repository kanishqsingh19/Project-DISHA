"""
AURA Conversation Processor

Connects incoming user messages to the conversation engine
and prepares them for the intelligence router.
"""

from .engine import ConversationEngine
from ..router.router import IntelligenceRouter


class ConversationProcessor:
    """Processes user messages for AURA."""

    def __init__(self):
        self.conversation = ConversationEngine()
        self.router = IntelligenceRouter()

    def process(self, message):
        """Process a user message."""
        self.conversation.add_message("user", message)

        routing_result = self.router.route(message)

        return {
            "status": "processed",
            "message": message,
            "routing": routing_result
        }
