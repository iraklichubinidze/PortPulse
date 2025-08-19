import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_LOGIN,
    SMTP_PASSWORD,
    SENDER_EMAIL,
    RECEIVER_EMAILS,
)


def send_email(
    smtp_server: str = SMTP_SERVER,
    smtp_port: int = SMTP_PORT,
    smtp_login: str = SMTP_LOGIN,
    smtp_password: str = SMTP_PASSWORD,
    sender_email: str = SENDER_EMAIL,
    receiver_emails: list = RECEIVER_EMAILS,
    html_file: str = None,
):
    """
    Send an HTML email with the given report file attached as body.
    """
    if not html_file:
        logging.error("No HTML file provided for email content.")
        return False

    try:
        with open(html_file, "r") as f:
            html_content = f.read()
    except FileNotFoundError:
        logging.error(f"HTML report file not found: {html_file}")
        return False
    except Exception as e:
        logging.error(f"Error reading HTML file {html_file}: {e}")
        return False

    message = MIMEMultipart("alternative")
    message["Subject"] = "Daily NetScan"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)

    part = MIMEText(html_content, "html")
    message.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_login, smtp_password)
            server.sendmail(sender_email, receiver_emails, message.as_string())

        logging.info("Email alert sent successfully.")
        return True

    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")
        return False
