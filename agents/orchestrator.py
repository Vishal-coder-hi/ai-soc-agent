from agents.detection_agent import detect_alerts
from agents.threat_intel_agent import enrich_alert
from agents.investigation_agent import investigate
from agents.response_agent import create_response

from analyzer.risk_scorer import calculate_risk
from analyzer.rag_engine import retrieve_knowledge
from analyzer.ai_analyst import analyze_alert


class SOCOrchestrator:
    """
    SOC Orchestrator

    Coordinates multiple specialized security agents
    and combines their results into one SOC workflow.
    """

    def __init__(self, log_file):
        self.log_file = log_file

    def run(self):
        print("\n===== SOC ORCHESTRATOR STARTED =====\n")

        # --------------------------------
        # 1. Detection Agent
        # --------------------------------
        print("[1] Detection Agent running...")

        alerts = detect_alerts(self.log_file)

        print(f"    Detected {len(alerts)} alerts.")

        # --------------------------------
        # 2. Threat Intelligence Agent
        # --------------------------------
        print("\n[2] Threat Intelligence Agent running...")

        enriched_alerts = []

        for alert in alerts:
            enriched = enrich_alert(alert)
            enriched_alerts.append(enriched)

        print("    Threat intelligence enrichment completed.")

        # --------------------------------
        # 3. Risk Assessment
        # --------------------------------
        print("\n[3] Risk Assessment running...")

        for alert in enriched_alerts:
            risk = calculate_risk(alert)

            alert["risk_score"] = risk["risk_score"]
            alert["risk_level"] = risk["risk_level"]

        print("    Risk scoring completed.")

        # --------------------------------
        # 4. Security RAG
        # --------------------------------
        print("\n[4] Security RAG running...")

        for alert in enriched_alerts:
            knowledge = retrieve_knowledge(alert)

            alert["security_knowledge"] = knowledge

        print("    Security knowledge retrieved.")

        # --------------------------------
        # 5. AI SOC Analyst
        # --------------------------------
        print("\n[5] AI SOC Analyst running...")

        for alert in enriched_alerts:
            alert["ai_analysis"] = analyze_alert(alert)

        print("    AI analysis completed.")

        # --------------------------------
        # 6. Investigation Agent
        # --------------------------------
        print("\n[6] Investigation Agent running...")

        investigation = investigate(enriched_alerts)

        print("    Incident investigation completed.")

        # --------------------------------
        # 7. Response Agent
        # --------------------------------
        print("\n[7] Response Agent running...")

        for alert in enriched_alerts:
            alert["response_plan"] = create_response(alert)

        print("    Response plans generated.")

        # --------------------------------
        # Final SOC Result
        # --------------------------------
        result = {
            "alerts": enriched_alerts,
            "investigation": investigation
        }

        print("\n===== SOC ORCHESTRATOR COMPLETED =====\n")

        return result