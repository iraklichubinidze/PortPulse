# PortPulse 🐍📊

**PortPulse** is a lightweight **Python network scanning and reporting tool** designed for IT pros, sysadmins, and network engineers. It automatically discovers live hosts, detects open ports, generates clean HTML reports, and can optionally send them via email.  

Turn raw Nmap output into actionable insights — **without manual effort**.  


## ⚡ Features

- Discover live hosts and open ports with **Nmap**  
- Generate **HTML reports** with summary boxes and charts
- **Email delivery** via SMTP  
- Fully configurable through `config.py`  
- Compatible with **cronjobs** for automated daily scans  


## 🐍 Installation

1. Clone the repository:  
```bash
git clone https://github.com/iraklichubinidze/PortPulse.git
cd PortPulse
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

> **Dependencies**:  
> - `jinja2` → HTML templating  
> - All other modules are **standard Python libraries** (`subprocess`, `os`, `smtplib`, `email`, `collections`, `ipaddress`)  

3. Add the **IP addresses or networks you want to scan** in the `ips.txt` file. Each IP or network should be on a separate line.  

4. Configure network and email settings in `config.py`.  

## ⚙️ Configuration (`config.py`)

### Nmap settings
```python
NMAP_PING_SCAN_OPTIONS = ["-sn"]
NMAP_SCAN_OPTIONS = ["-sV", "-p-", "--open"]
```
- Ping scan discovers live hosts quickly.  
- Full port scan with service/version detection shows **open ports only**.  

### Output filtering
```python
ENABLE_OUTPUT_FILTERING = True
FILTER_KEYWORDS = ["tcpwrapped"]
```
- Filters out `"tcpwrapped"` lines, which typically indicate **firewall-protected ports**, keeping reports clean and relevant.  

### Email settings
```python
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_LOGIN = "<YOUR_SMTP_LOGIN>"
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SENDER_EMAIL = "<SENDER_EMAIL>"
RECEIVER_EMAILS = ["<ADD_EMAIL_1>","<ADD_EMAIL_2>"]
EMAIL_SUBJECT = "Daily NetScan"
```
- Configure your SMTP credentials to automatically send reports.  
- **Security tip:** Set `SMTP_PASSWORD` as an environment variable (in ```~/.bashrc```):
```bash
export SMTP_PASSWORD="yourpassword"
```

## 🚀 Usage

Run the tool manually:  
```bash
python main.py
```

- Scans hosts listed in `ips.txt`  
- Saves HTML report to `output/scan_report.html`  
- Emails the report if SMTP is configured  



## 📂 Output
- HTML report: `output/scan_report.html`  
- Logs (optional if using cron)  

## 🕖 Automate with Cronjobs

Run **PortPulse** automatically every day at 7:00 AM

1. Open crontab:  
```bash
crontab -e
```

2. Add this line:  
```bash
0 7 * * * /usr/bin/python3 /path/to/PortPulse/main.py >> /path/to/PortPulse/cron.log 2>&1
```

This runs the script daily at 7:00 AM and logs output to `cron.log`.  

