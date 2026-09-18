import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("QWEN_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://ws-59mgowi0mha0m6y5.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)


def build_investigation(alerts):
    """
    Correlates multiple security alerts and sends
    the complete incident context to the AI.
    """

    investigation = {
        "total_alerts": len(alerts),
        "high_severity": [],
        "medium_severity": [],
        "possible_attack_chain": []
    }

    # Categorize alerts
    for alert in alerts:

        severity = alert.get("severity")

        if severity == "HIGH":
            investigation["high_severity"].append(alert)

        elif severity == "MEDIUM":
            investigation["medium_severity"].append(alert)

    # Basic attack-chain detection
    threats = [alert.get("threat", "") for alert in alerts]

    if "Port Scanning" in threats:
        investigation["possible_attack_chain"].append(
            "Network reconnaissance detected"
        )

    if "Possible Brute Force Attack" in threats:
        investigation["possible_attack_chain"].append(
            "Credential attack detected"
        )

    if "Sensitive File Access" in threats:
        investigation["possible_attack_chain"].append(
            "Sensitive system information accessed"
        )

    if "Failed Privilege Escalation" in threats:
        investigation["possible_attack_chain"].append(
            "Privilege escalation attempt detected"
        )

    # Prepare complete evidence for AI
    evidence = "\n".join(
        [
            f"Alert {i + 1}: {alert}"
            for i, alert in enumerate(alerts)
        ]
    )

    prompt = f"""
You are an expert Cybersecurity SOC Investigation Agent.

You have received multiple security alerts from a security monitoring system.

Your task is to correlate these alerts and determine whether
they could represent a single attack campaign or related activity.

Security Alerts:

{evidence}

Provide an incident investigation report with exactly these sections:

1. Overall Incident Assessment
2. Overall Severity
3. Possible Attack Chain
4. Attacker Objective
5. Investigation Priority
6. Recommended Defensive Response

Important:
- Do not assume that the alerts definitely belong to one attacker.
- Clearly distinguish confirmed evidence from possible relationships.
- Do not invent missing IP addresses, users, timestamps, or events.
- Give practical SOC investigation recommendations.
- Keep the report concise but useful.
"""

    try:

        response = client.chat.completions.create(
            model="qwen-plus-character",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional SOC incident "
                        "investigation analyst."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        investigation["ai_report"] = response.choices[0].message.content

    except Exception as error:

        investigation["ai_report"] = (
            f"AI investigation failed: {error}"
        )

    return investigation