from analyzer.response_agent import generate_response


test_alert = {
    "ip": "185.220.101.5",
    "failed_attempts": 5,
    "threat": "Possible Brute Force Attack",
    "severity": "HIGH",
    "description": "5 failed login attempts detected.",
    "risk_score": 86,
    "risk_level": "CRITICAL"
}


print("\n===== SOC RESPONSE AGENT =====\n")

response = generate_response(test_alert)

print(response)