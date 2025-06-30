import json

def log_traffic(headers, body):
    with open("burp_traffic.json", "a") as file:
        json.dump({"headers": headers, "body": body}, file)
