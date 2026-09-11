"""
AURA Request Classifier

Provides a basic foundation for identifying request types.
"""


class RequestClassifier:
    """Classifies user requests into broad categories."""

    def classify(self, request):
        """Return a basic category for a user request."""

        text = request.lower()

        if any(word in text for word in ["calculate", "math", "sum"]):
            return "calculation"

        if any(word in text for word in ["search", "find", "research"]):
            return "research"

        if any(word in text for word in ["file", "folder", "document"]):
            return "file_operation"

        if any(word in text for word in ["open", "close", "launch"]):
            return "computer_action"

        return "general"
