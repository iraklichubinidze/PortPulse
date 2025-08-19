import logging
import os
from scanner import scan_ips
from report_generator import generate_html_report
from emailer import send_email

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_LOGIN,
    SMTP_PASSWORD,
    SENDER_EMAIL,
    RECEIVER_EMAILS,
    EMAIL_SUBJECT
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def main():
    logging.info("Starting Nmap scan...")
    scan_results = scan_ips("ips.txt","output")
    logging.info("Nmap scan completed.")

    logging.info("Generating HTML report...")
    html_report_path = generate_html_report(scan_results, "output")
    logging.info(f"HTML report saved at: {html_report_path}")

    logging.info("Sending email with the report...")
    send_email(
        SMTP_SERVER,
        SMTP_PORT,
        SMTP_LOGIN,
        SMTP_PASSWORD,
        SENDER_EMAIL,
        RECEIVER_EMAILS,
        html_report_path,
        EMAIL_SUBJECT
    )
    logging.info("Email sent successfully.")


if __name__ == "__main__":
    main()
