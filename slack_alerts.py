import requests
from config import SLACK_WEBHOOK_URL

def send_slack_alert(message):
    if not SLACK_WEBHOOK_URL:
        print("[Slack] NO webhook url set")
        return
    payload = {
        "text" : message
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code != 200:
            print(f"[Slack] Failed: {response.status_code}, {response.text}")
    except Exception as e:
        print('[Slack] error: {e}')