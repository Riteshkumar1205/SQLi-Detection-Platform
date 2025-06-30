import json
import time
import os
from core.detection import SQLiDetector
from datetime import datetime

def monitor_traffic(file_path):
    detector = SQLiDetector()
    seen = set()
    print(f"[🔍] Watching {file_path} for SQLi attempts...")

    while True:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.read().splitlines()

                for line in lines:
                    if line in seen:
                        continue
                    seen.add(line)

                    try:
                        data = json.loads(line)
                        body = data.get("body", "")
                        if detector.is_sqli(body):
                            print(f"[⚠️] SQLi Detected! Body: {body}")
                            with open("burpsuite/detected_sqli.log", "a") as log:
                                log.write(f"{datetime.now()} :: {body}\n")
                    except Exception as e:
                        print(f"[!] Error parsing line: {e}")

        time.sleep(2)

if __name__ == "__main__":
    monitor_traffic("burp_traffic.json")
