# === core/detection.py ===
import re

class SQLiDetector:
    def __init__(self):
        self.patterns = [
            r"(?i)(\%27)|(')|(--)|(\%23)|(#)",
            r"(?i)(\bOR\b|\bAND\b).*(=)",
            r"(?i)UNION(\s)+SELECT",
            r"(?i)DROP(\s)+TABLE",
            r"(?i)INSERT(\s)+INTO",
            r"(?i)UPDATE(\s)+.*SET",
        ]

    def is_sqli(self, input_data):
        for pattern in self.patterns:
            if re.search(pattern, input_data):
                return True
        return False
