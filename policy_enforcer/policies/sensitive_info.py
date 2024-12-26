import re

class SensitiveInfo:
    def __init__(self):
        self.patterns = {
            "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "PHONE": r"(\+65\s?\d{8}|\b\d{8}\b)",  # Singapore phone numbers
            "NRIC": r"\b[S,T]\d{7}[A-Z]\b"         # Singapore NRIC/FIN format
        }

    def mask(self, text: str) -> str:
        for key, pattern in self.patterns.items():
            text = re.sub(pattern, f"[{key}]", text)
        return text
