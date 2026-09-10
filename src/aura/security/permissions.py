"""
AURA Permission Manager

Controls whether AURA is allowed to perform an action.
"""


class PermissionManager:
    """Manages user permissions for AURA actions."""

    def __init__(self):
        self.permissions = {}

    def grant(self, action):
        """Grant permission for an action."""
        self.permissions[action] = True

    def revoke(self, action):
        """Revoke permission for an action."""
        self.permissions[action] = False

    def is_allowed(self, action):
        """Check whether an action is currently allowed."""
        return self.permissions.get(action, False)
