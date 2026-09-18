from flask import Flask, render_template

from analyzer.log_parser import analyze_logs
from analyzer.threat_intel import lookup_ip
from analyzer.risk_scorer import calculate_risk
from analyzer.rag_engine import retrieve_knowledge
from analyzer.ai_analyst import analyze_alert
from analyzer.response_agent import generate_response

from analyzer.storage import (
    load_results,
    save_results,
    find_cached_alert
)


app = Flask(__name__)

LOG_FILE = "logs/security.log"


def process_alert(alert):
    """
    Process a new alert through the complete SOC pipeline.
    """

    enriched_alert = alert.copy()

    # --------------------------------
    # 1. Threat Intelligence
    # --------------------------------

    if "ip" in alert:

        enriched_alert["threat_intelligence"] = lookup_ip(
            alert["ip"]
        )

    # --------------------------------
    # 2. Risk Scoring
    # --------------------------------

    risk = calculate_risk(enriched_alert)

    enriched_alert["risk_score"] = risk["risk_score"]
    enriched_alert["risk_level"] = risk["risk_level"]

    # --------------------------------
    # 3. Security RAG
    # --------------------------------

    knowledge = retrieve_knowledge(
        enriched_alert
    )

    enriched_alert["security_knowledge"] = knowledge

    # --------------------------------
    # 4. AI SOC Analysis
    # --------------------------------

    enriched_alert["ai_analysis"] = analyze_alert(
        enriched_alert
    )

    # --------------------------------
    # 5. Response Agent
    # --------------------------------

    enriched_alert["response_plan"] = generate_response(
        enriched_alert
    )

    return enriched_alert


def get_dashboard_data():

    alerts = analyze_logs(LOG_FILE)

    stored_results = load_results()

    final_results = []

    for alert in alerts:

        # Check whether this alert was already processed
        cached_alert = find_cached_alert(
            alert,
            stored_results
        )

        if cached_alert:

            print(
                f"Using cached result: "
                f"{alert.get('threat')}"
            )

            final_results.append(
                cached_alert
            )

        else:

            print(
                f"Processing new alert: "
                f"{alert.get('threat')}"
            )

            processed_alert = process_alert(
                alert
            )

            final_results.append(
                processed_alert
            )

    # Save current results
    save_results(final_results)

    return final_results


@app.route("/")
def dashboard():

    alerts = get_dashboard_data()

    total_alerts = len(alerts)

    critical = sum(
        1
        for alert in alerts
        if alert["risk_level"] == "CRITICAL"
    )

    high = sum(
        1
        for alert in alerts
        if alert["risk_level"] == "HIGH"
    )

    medium = sum(
        1
        for alert in alerts
        if alert["risk_level"] == "MEDIUM"
    )

    low = sum(
        1
        for alert in alerts
        if alert["risk_level"] == "LOW"
    )

    return render_template(
        "index.html",
        alerts=alerts,
        total_alerts=total_alerts,
        critical=critical,
        high=high,
        medium=medium,
        low=low
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )