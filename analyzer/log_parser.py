from collections import defaultdict


def analyze_logs(file_path):
    failed_attempts = defaultdict(int)
    alerts = []

    with open(file_path, "r") as file:
        for line in file:

            # 1. Brute Force Detection
            if "Login failed" in line:
                parts = line.split("ip=")

                if len(parts) == 2:
                    ip = parts[1].strip()
                    failed_attempts[ip] += 1

            # 2. Sensitive File Access
            if "file=/etc/passwd" in line:
                alerts.append({
                    "threat": "Sensitive File Access",
                    "severity": "MEDIUM",
                    "description": "The /etc/passwd file was accessed."
                })

            # 3. Port Scan Detection
            if "Port scan detected" in line:
                parts = line.split("source=")

                if len(parts) == 2:
                    source_ip = parts[1].split()[0]

                    alerts.append({
                        "ip": source_ip,
                        "threat": "Port Scanning",
                        "severity": "HIGH",
                        "description": "Multiple ports were scanned."
                    })

            # 4. Privilege Escalation Detection
            if "Privilege escalation failed" in line:
                alerts.append({
                    "threat": "Failed Privilege Escalation",
                    "severity": "HIGH",
                    "description": "A privilege escalation attempt failed."
                })

    # Brute force alerts
    for ip, count in failed_attempts.items():

        if count >= 5:
            alerts.append({
                "ip": ip,
                "failed_attempts": count,
                "threat": "Possible Brute Force Attack",
                "severity": "HIGH",
                "description": f"{count} failed login attempts detected."
            })

    return alerts