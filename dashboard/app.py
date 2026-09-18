from flask import Flask, render_template

from core.soc_pipeline import SOCPipeline
from services.incident_store import load_incidents


app = Flask(__name__)

LOG_FILE = "logs/security.log"


@app.route("/")
def dashboard():

    incidents = load_incidents()

    latest_incident = None

    if incidents:
        latest_incident = incidents[-1]

    alerts = []

    if latest_incident:
        alerts = latest_incident.get("alerts", [])

    total_alerts = len(alerts)

    critical = sum(
        1 for alert in alerts
        if alert.get("risk_level") == "CRITICAL"
    )

    high = sum(
        1 for alert in alerts
        if alert.get("risk_level") == "HIGH"
    )

    medium = sum(
        1 for alert in alerts
        if alert.get("risk_level") == "MEDIUM"
    )

    low = sum(
        1 for alert in alerts
        if alert.get("risk_level") == "LOW"
    )

    return render_template(
        "index.html",
        alerts=alerts,
        total_alerts=total_alerts,
        critical=critical,
        high=high,
        medium=medium,
        low=low,
        latest_incident=latest_incident,
        incidents=incidents
    )


@app.route("/run-scan")
def run_scan():

    pipeline = SOCPipeline(LOG_FILE)

    pipeline.process()

    return """
    <h2>SOC Scan Completed</h2>
    <p>AI SOC pipeline processed the security logs successfully.</p>
    <a href="/">Return to Dashboard</a>
    """


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )