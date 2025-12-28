import os

from dotenv import load_dotenv

load_dotenv()

CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 85))
BATTERY_THRESHOLD = int(os.getenv("BATTERY_THRESHOLD", 20))

CPU_ALERT_INTERVAL = int(os.getenv("CPU_ALERT_INTERVAL", 30))
BATTERY_ALERT_INTERVAL = int(os.getenv("BATTERY_ALERT_INTERVAL", 60))

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS")