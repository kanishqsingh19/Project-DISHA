"""
AURA Intelligence Router

Responsible for selecting the appropriate intelligence
source for a user request.
"""


class IntelligenceRouter:
    """Routes requests to the appropriate AI capability."""

    def route(self, request):
        """
        Determine where a request should be handled.

        Routing logic will be implemented later.
        """
        return {
            "status": "pending",
            "request": request,
            "provider": None
        }
