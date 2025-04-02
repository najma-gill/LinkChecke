# error_summary.py

class ErrorSummary:
    def __init__(self):
        # Initialize an empty list to store error messages and parameters
        self.errors = []

    def add_error(self, parameter, message):
        # Add an error message with the associated parameter
        self.errors.append({'parameter': parameter, 'message': message})

    def get_summary(self):
        # Generate a summary of all errors
        if not self.errors:
            return "No errors found."
        
        summary_lines = ["Error Summary:"]
        for error in self.errors:
            summary_lines.append(f"Parameter: {error['parameter']}, Error: {error['message']}")
        
        return "\n".join(summary_lines)