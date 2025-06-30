import re

# SQL injection patterns (case-insensitive)
SQLI_PATTERNS = [
    r"union.*select",
    r"or\s+\d+=\d+",
    r"or\s+'[^']*'='[^']*'",
    r"(\%27)|(')",
    r"select.+from",
    r"drop\s+table",
    r"insert\s+into",
    r"--|#|/\*",
    r"benchmark\s*\(\s*\d+,\s*.*\)",
    r"sleep\s*\(\s*\d+\s*\)",
    r"waitfor\s+delay"
]

def is_sqli(payload: str) -> bool:
    return any(re.search(pattern, payload, re.IGNORECASE) for pattern in SQLI_PATTERNS)
