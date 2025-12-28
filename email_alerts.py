import smtplib
from email.message import EmailMessage
import os
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, TO_ADDRESS

def send_email_alert(subject: str, logger, body: str):
    if not all([EMAIL_ADDRESS, EMAIL_PASSWORD, TO_ADDRESS]):
        msg = "Email alert skipped: missing EMAIL_ADDRESS, EMAIL_PASSWORD or TO_ADDRESS"
        logger.info(msg)
        return
    msg = EmailMessage()
    msg["Subject"] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        logger.info(f"Email Failed: {e}")