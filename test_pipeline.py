from core.soc_pipeline import SOCPipeline


LOG_FILE = "logs/security.log"


print("\n===================================")
print("        AI SOC PIPELINE TEST")
print("===================================\n")


pipeline = SOCPipeline(LOG_FILE)

result = pipeline.process()


print("\n===== PIPELINE RESULT =====")

print(f"Total Alerts: {len(result['alerts'])}")

for alert in result["alerts"]:
    print("\n--------------------------------")
    print(f"Threat: {alert.get('threat')}")
    print(f"Severity: {alert.get('severity')}")
    print(f"Risk Score: {alert.get('risk_score')}")
    print(f"Risk Level: {alert.get('risk_level')}")

print("\nInvestigation Generated:")
print("YES" if result.get("investigation") else "NO")


print("\n===================================")
print("       PIPELINE TEST COMPLETE")
print("===================================\n")