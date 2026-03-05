
"""
LLM-based Root Cause Analysis for OpsSentry
"""

class RCALLM:

    def analyze_failure(self, log_text: str) -> dict:
        """
        Simple AI-based log analysis.
        (Later we can plug GPT or Llama here)
        """

        log_text = log_text.lower()

        if "modulenotfounderror" in log_text:
            return {
                "root_cause": "Missing Python dependency",
                "fix": "Add the missing package to requirements.txt and reinstall dependencies."
            }

        elif "timeout" in log_text:
            return {
                "root_cause": "Pipeline step timeout",
                "fix": "Increase timeout or optimize the build step."
            }

        elif "permission denied" in log_text:
            return {
                "root_cause": "Permission issue",
                "fix": "Check file permissions or CI/CD credentials."
            }

        else:
            return {
                "root_cause": "Unknown failure",
                "fix": "Check logs manually for more details."
            }
