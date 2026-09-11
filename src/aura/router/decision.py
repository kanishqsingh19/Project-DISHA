"""
AURA Routing Decision

Provides the foundation for intelligent provider selection.
"""
from .classifier import RequestClassifier

class RoutingDecision:
    """Makes routing decisions for AURA."""

    def __init__(self):
        self.providers = [
            "local",
            "cloud",
            "specialized"
        ]
        
        self.classifier = RequestClassifier()

        def choose(self, request, available_providers):
        """Choose a provider based on the request type."""

        request_type = self.classifier.classify(request)

        if request_type == "file_operation":
            preferred = ["local", "cloud", "specialized"]

        elif request_type == "research":
            preferred = ["cloud", "specialized", "local"]

        elif request_type == "calculation":
            preferred = ["local", "cloud", "specialized"]

        elif request_type == "computer_action":
            preferred = ["local", "cloud", "specialized"]

        else:
            preferred = ["cloud", "local", "specialized"]

        for provider in preferred:
            if provider in available_providers:
                return provider

        return None
