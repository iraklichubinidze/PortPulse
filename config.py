import os

# --- Nmap configuration ---
NMAP_PING_SCAN_OPTIONS = ["-sn"]  # Ping scan only - Default
NMAP_SCAN_OPTIONS = ["-sV", "--open"]  # Service/version detection, all ports, open only - Default

# --- Output filtering ---
ENABLE_OUTPUT_FILTERING = True # Default
FILTER_KEYWORDS = ["tcpwrapped"] # Default

# --- Email settings --- 
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_LOGIN = "<YOUR_MAIL>" # Change this
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "") # You should add in .bashrc (export SMTP_PASSWORD="<PASSWORD_HERE>") 
SENDER_EMAIL = "<SENDER>" # Change this
RECEIVER_EMAILS = ["<MAIL1>", "<MAIL2>"] # Change This
EMAIL_SUBJECT = "PortPulse - Daily NetScan"
