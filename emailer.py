# emailer.py
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
