# PortPulse 🐍📊

**PortPulse** is a lightweight **Python network scanning and reporting tool** designed for IT pros, sysadmins, and network engineers. It automatically discovers live hosts, detects open ports, generates clean HTML reports, and can optionally send them via email.  

Turn raw Nmap output into actionable insights — **without manual effort**.  

```

## ⚡ Features

- Discover live hosts and open ports with **Nmap**  
- Generate **HTML reports** with summary boxes and charts  
- Optional **email delivery** via SMTP  
- Fully configurable through `config.py`  
- Compatible with **cronjobs** for automated daily scans  

```

## 🐍 Installation

1. Clone the repository:  
```
git clone https://github.com/yourusername/PortPulse.git
cd PortPulse
```

2. Install dependencies:  
```
pip install -r requirements.txt
```

> **Dependencies**:  
> - `jinja2` → HTML templating  
> - All other modules are **standard Python libraries** (`subprocess`, `os`, `smtplib`, `email`, `collections`, `ipaddress`)  

3. Add the **IP addresses or networks you want to scan** in the `ips.txt` file. Each IP or network should be on a separate line.  

4. Configure network and email settings in `config.py`.  

```

## 🚀 Usage

Run the tool manually:  
```
python main.py
```

- Scans hosts listed in `ips.txt`  
- Saves HTML report to `output/scan_report.html`  
- Optionally emails the report if SMTP is configured  

```

## 🕖 Automate with Cronjobs

Run **PortPulse** automatically every day at 7:00 AM

1. Open crontab:  
```
crontab -e
```

2. Add this line:  
```
0 7 * * * /usr/bin/python3 /path/to/PortPulse/main.py >> /path/to/PortPulse/cron.log 2>&1
```

This runs the script daily at 7:00 AM and logs output to `cron.log`.  

```

## ⚙️ Configuration (`config.py`)

### Nmap settings
```
NMAP_PING_SCAN_OPTIONS = ["-sn"]
NMAP_SCAN_OPTIONS = ["-sV", "-p-", "--open"]
```

- Ping scan discovers live hosts quickly.  
- Full port scan with service/version detection shows **open ports only**.  

### Output filtering
```
ENABLE_OUTPUT_FILTERING = True
FILTER_KEYWORDS = ["tcpwrapped"]
```

- Filters out `"tcpwrapped"` lines, which typically indicate **firewall-protected ports**, keeping reports clean and relevant.  

### Paths
```
INPUT_FILE = "ips.txt"
OUTPUT_DIR = "output"
```

- Fixed paths for input and output files.  

### Email settings
```
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SMTP_LOGIN = "<YOUR_SMTP_LOGIN>"
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SENDER_EMAIL = "<SENDER_EMAIL>"
RECEIVER_EMAILS = ["list@example.com"]
EMAIL_SUBJECT = "Daily NetScan"
```

- Configure your SMTP credentials to automatically send reports.  
- **Security tip:** Set `SMTP_PASSWORD` as an environment variable:  
```
export SMTP_PASSWORD="yourpassword"
```

### Report settings
```
TEMPLATE_DIR = "templates"
REPORT_TEMPLATE = "report_template.html"
REPORT_OUTPUT_FILE = "scan_report.html"
```

- Defines template folder and report filename — required for report generation.  

```

## 📂 Output

- HTML report: `output/scan_report.html`  
- Logs (optional if using cron)  

```

## 🧑‍💻 Why PortPulse?

- Save time by automating **network discovery and reporting**  
- Get **daily actionable insights** without opening terminals  
- Lightweight, flexible, and easy to configure  

```

## 📌 License

MIT License © [Your Name]  
