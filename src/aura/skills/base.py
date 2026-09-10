"""
AURA Skill Interface

Defines the common structure for AURA skills.
"""


class Skill:
    """Base interface for an AURA skill."""

    name = "unnamed"

    def execute(self, request):
        """
        Execute the skill.

        Individual skills will implement this method.
        """
        raise NotImplementedError(
            "Skills must implement the execute method."
        )
