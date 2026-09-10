"""
AURA Conversation Engine

Responsible for managing the basic conversation flow.
"""


class ConversationEngine:
    """Core conversation manager for AURA."""

    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        """Add a message to the current conversation."""
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        """Return the current conversation history."""
        return self.history

    def clear_history(self):
        """Clear the current conversation."""
        self.history.clear()
