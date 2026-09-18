from agents.detection_agent import detect_alerts
from agents.threat_intel_agent import enrich_alert
from agents.investigation_agent import investigate
from agents.response_agent import create_response


LOG_FILE = "logs/security.log"


print("\n===== MULTI-AGENT SOC TEST =====\n")


# 1. Detection Agent
alerts = detect_alerts(LOG_FILE)

print(f"Detection Agent: {len(alerts)} alerts detected.")


# 2. Threat Intelligence Agent
enriched_alerts = []

for alert in alerts:

    enriched = enrich_alert(alert)

    enriched_alerts.append(enriched)

print("Threat Intelligence Agent: Alerts enriched.")


# 3. Investigation Agent
investigation = investigate(enriched_alerts)

print(
    "Investigation Agent: "
    "Incident investigation generated."
)


# 4. Response Agent
if enriched_alerts:

    response = create_response(
        enriched_alerts[0]
    )

    print(
        "Response Agent: "
        "Response plan generated."
    )


print("\n===== MULTI-AGENT TEST COMPLETE =====")