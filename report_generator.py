import os
import logging
from collections import Counter
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def parse_scan_results(scan_results: dict):
    """
    Parse raw Nmap scan output and return structured results and all open ports.
    Returns: (structured_results: dict, all_ports: list)
    """
    structured_results = {}
    all_ports = []

    for ip, raw_result in scan_results.items():
        open_ports = []
        for line in raw_result.splitlines():
            if "/tcp" in line or "/udp" in line:
                parts = line.split()
                if len(parts) >= 3:
                    port_state = parts[0].split('/')[0]
                    state = parts[1]
                    service_version = " ".join(parts[2:])
                    if state.lower() == "open":
                        open_ports.append((port_state, state, service_version))
                        all_ports.append(port_state)
        if open_ports:
            structured_results[ip] = open_ports

    return structured_results, all_ports


def generate_summary_html(total_hosts: int, hosts_with_open_ports: int, all_total_ports: str):
    """Generate HTML for summary boxes."""
    return f"""
    <div class="summary-container">
        <div class="summary-box">
            <h3>Total Hosts Scanned</h3>
            <p>{total_hosts}</p>
        </div>
        <div class="summary-box">
            <h3>Total Open Ports</h3>
            <p>{all_total_ports}</p>
        </div>
        <div class="summary-box">
            <h3>Hosts with Open Ports</h3>
            <p>{hosts_with_open_ports}</p>
        </div>
    </div>
    """


def generate_chart_html(port_counter: Counter):
    """Generate HTML and JS for the bar chart of open ports."""
    port_labels = list(port_counter.keys())
    port_counts = list(port_counter.values())

    return f"""
    <canvas id="portsChart"></canvas>
    <script>
        const ctx = document.getElementById('portsChart').getContext('2d');
        new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: {port_labels},
                datasets: [{{
                    label: 'Open Port Frequency',
                    data: {port_counts},
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{ display: false }},
                    title: {{ display: true, text: 'Most Common Open Ports' }}
                }},
                scales: {{
                    y: {{ beginAtZero: true }}
                }}
            }}
        }});
    </script>
    """


def generate_html_report(scan_results: dict, output_dir: str) -> str:
    """
    Generate an HTML report from Nmap scan results.
    Returns the path to the generated report file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    structured_results, all_ports = parse_scan_results(scan_results)
    total_hosts = len(scan_results)
    hosts_with_open_ports = len(structured_results)
    port_counter = Counter(all_ports)
    all_ports_sum = str(sum(port_counter.values()))

    summary_html = generate_summary_html(total_hosts, hosts_with_open_ports, all_ports_sum)
    chart_html = generate_chart_html(port_counter)

    try:
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("report_template.html")
        report_html = template.render(
            results=structured_results,
            summary_html=summary_html,
            chart_html=chart_html
        )
    except Exception as e:
        logging.error(f"Failed to load template or render report: {e}")
        return ""

    output_file = os.path.join(output_dir, "scan_report.html")
    with open(output_file, "w") as f:
        f.write(report_html)

    logging.info(f"HTML report generated: {output_file}")
    return output_file

