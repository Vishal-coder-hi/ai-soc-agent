import json
import os
from datetime import datetime


INCIDENT_FILE = "storage/incidents.json"


def load_incidents():
    """
    Load previously stored SOC incidents.
    """

    if not os.path.exists(INCIDENT_FILE):
        return []

    try:
        with open(INCIDENT_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_incident(incident):
    """
    Save a new SOC incident.
    """

    incidents = load_incidents()

    incident["incident_id"] = f"INC-{len(incidents) + 1:04d}"
    incident["created_at"] = datetime.now().isoformat()

    incidents.append(incident)

    os.makedirs(os.path.dirname(INCIDENT_FILE), exist_ok=True)

    with open(INCIDENT_FILE, "w") as file:
        json.dump(incidents, file, indent=4)

    return incident


def get_incident(incident_id):
    """
    Retrieve a specific incident by ID.
    """

    incidents = load_incidents()

    for incident in incidents:
        if incident.get("incident_id") == incident_id:
            return incident

    return None