from services.incident_store import (
    save_incident,
    load_incidents,
    get_incident
)


print("\n===================================")
print("      INCIDENT STORE TEST")
print("===================================\n")


incident = {
    "severity": "CRITICAL",
    "risk_score": 86,
    "threat": "Possible Brute Force Attack",
    "status": "OPEN"
}


saved = save_incident(incident)

print("Incident saved:")
print(f"ID: {saved['incident_id']}")
print(f"Threat: {saved['threat']}")
print(f"Risk Score: {saved['risk_score']}")


incidents = load_incidents()

print(f"\nTotal stored incidents: {len(incidents)}")


retrieved = get_incident(saved["incident_id"])

print("\nIncident retrieval:")

if retrieved:
    print("SUCCESS")
    print(f"Retrieved ID: {retrieved['incident_id']}")
else:
    print("FAILED")


print("\n===================================")
print("       STORAGE TEST COMPLETE")
print("===================================\n")