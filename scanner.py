import subprocess
import os
from config import NMAP_SCAN_OPTIONS

def get_live_ips(network):
    try:
        cmd = ["nmap", "-sn", network, "-oG", "-"]
        print(f"Running Nmap ping scan for network: {network}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        live_ips = []

        for line in result.stdout.splitlines():
            if "Host:" in line and "Status: Up" in line:
                parts = line.split()
                ip = parts[1]
                live_ips.append(ip)

        return live_ips
    except Exception as e:
        print(f"Error discovering live hosts for network {network}: {e}")
        return []

def is_valid_ip_or_network(entry):
    try:
        import ipaddress
        ipaddress.ip_network(entry, strict=False)
        return True
    except ValueError:
        return False

def scan_ips(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    results = {}
    with open(input_file, 'r') as f:
        ips_or_networks = [line.strip() for line in f.readlines()]

    print(f"Loaded IPs/Networks from {input_file}: {ips_or_networks}")

    for item in ips_or_networks:
        if not item:
            print("Skipping empty entry.")
            continue

        if not is_valid_ip_or_network(item):
            print(f"Skipping invalid entry: {item}")
            continue

        print(f"Processing {item}...")

        live_ips = []
        if '/' in item:
            live_ips = get_live_ips(item)
        else:
            live_ips = [item]

        print(f"Live IPs discovered for {item}: {live_ips}")

        for ip in live_ips:
            sanitized_ip = ip.replace("/", "_")
            output_file = os.path.join(output_dir, f"{sanitized_ip}.txt")
            cmd = ["nmap", ip] + NMAP_SCAN_OPTIONS + ["-oN", output_file]
            print(f"Running Nmap scan for IP: {ip}")

            subprocess.run(cmd, stdout=subprocess.DEVNULL)

            if os.path.exists(output_file):
                filtered_results = []
                with open(output_file, 'r') as result_file:
                    for line in result_file:
                        if "tcpwrapped" not in line:
                            filtered_results.append(line)

                # Save filtered results back to the same file
                with open(output_file, 'w') as result_file:
                    result_file.writelines(filtered_results)

                with open(output_file, 'r') as result_file:
                    results[ip] = result_file.read()
            else:
                print(f"Scan for {ip} failed or no results saved.")

    return results

