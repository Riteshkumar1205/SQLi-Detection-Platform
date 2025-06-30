from flask import request, abort
from core.detection import SQLiDetector

def detect_sql_injection():
    detector = SQLiDetector()
    for key, value in request.values.items():
        if detector.is_sqli(value):
            abort(403, description="Possible SQL Injection Detected!")
