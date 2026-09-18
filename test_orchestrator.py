from agents.orchestrator import SOCOrchestrator


LOG_FILE = "logs/security.log"


print("\n===================================")
print("      AI MULTI-AGENT SOC TEST")
print("===================================\n")


soc = SOCOrchestrator(LOG_FILE)

result = soc.run()


print("\n===== FINAL SOC SUMMARY =====")

print(f"Total Alerts: {len(result['alerts'])}")

for alert in result["alerts"]:
    print("\n--------------------------------")
    print(f"Threat: {alert.get('threat')}")
    print(f"Severity: {alert.get('severity')}")
    print(f"Risk Score: {alert.get('risk_score')}")
    print(f"Risk Level: {alert.get('risk_level')}")

print("\n===================================")
print("       MULTI-AGENT SOC COMPLETE")
print("===================================\n")