# PortPulse 🐍📊

**PortPulse** is a lightweight **Python network scanning and reporting tool** designed for IT pros, sysadmins, and network engineers. It automatically discovers live hosts, detects open ports, generates clean HTML reports, and can optionally send them via email.  

Turn raw Nmap output into actionable insights — **without manual effort**.  

---

## ⚡ Features

- Discover live hosts and open ports with **Nmap**  
- Generate **HTML reports** with summary boxes and charts  
- Optional **email delivery** via SMTP  
- Fully configurable through `config.py`  
- Compatible with **cronjobs** for automated daily scans  

---

## 🐍 Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/PortPulse.git
cd PortPulse
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Configure network and email settings in config.py:

## 🚀 Usage
### Run the tool manually:
```bash
python main.py
```

- Scans hosts listed in ips.txt
- Saves HTML report to output/scan_report.html
- Optionally emails the report if SMTP is configured

## 🕖 Automate with Cronjobs

Run **PortPulse** automatically every day at 7:00 AM:

1. Open crontab:
```bash
crontab -e
```
2. Add this line:
0 7 * * * /usr/bin/python3 /path/to/PortPulse/main.py >> /path/to/PortPulse/cron.log 2>&1

- This runs the script daily at 7:00 AM and logs output to cron.log.

