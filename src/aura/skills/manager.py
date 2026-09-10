"""
AURA Skill Manager

Registers and manages available AURA skills.
"""

from .base import Skill


class SkillManager:
    """Manages the skills available to AURA."""

    def __init__(self):
        self.skills = {}

    def register(self, skill):
        """Register a skill."""
        if not isinstance(skill, Skill):
            raise TypeError("Only Skill instances can be registered.")

        self.skills[skill.name] = skill

    def get_skill(self, name):
        """Return a registered skill by name."""
        return self.skills.get(name)

    def list_skills(self):
        """Return the names of registered skills."""
        return list(self.skills.keys())

    def execute(self, name, request):
        """Execute a registered skill."""
        skill = self.get_skill(name)

        if skill is None:
            return {
                "status": "error",
                "message": f"Skill '{name}' is not available."
            }

        return skill.execute(request)
