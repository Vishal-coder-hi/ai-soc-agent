from agents.detection_agent import detect_alerts
from agents.threat_intel_agent import enrich_alert
from agents.investigation_agent import investigate
from agents.response_agent import create_response

from analyzer.risk_scorer import calculate_risk
from analyzer.rag_engine import retrieve_knowledge
from analyzer.ai_analyst import analyze_alert

from services.incident_store import save_incident
from core.logger import logger


class SOCPipeline:
    """
    Central AI SOC processing pipeline.
    """

    def __init__(self, log_file):
        self.log_file = log_file

    def process(self):

        logger.info("SOC pipeline started")

        # -----------------------------
        # 1. Detection
        # -----------------------------

        try:
            alerts = detect_alerts(self.log_file)

            logger.info(
                "Detection completed | alerts=%s",
                len(alerts)
            )

        except Exception as error:

            logger.exception(
                "Detection failed: %s",
                error
            )

            return {
                "alerts": [],
                "investigation": {},
                "status": "FAILED",
                "error": "Detection stage failed"
            }

        enriched_alerts = []

        # -----------------------------
        # Process alerts
        # -----------------------------

        for alert in alerts:

            try:

                # Threat Intelligence
                enriched = enrich_alert(alert)

                # Risk Assessment
                risk = calculate_risk(enriched)

                enriched["risk_score"] = risk["risk_score"]
                enriched["risk_level"] = risk["risk_level"]

                # Security RAG
                knowledge = retrieve_knowledge(enriched)

                enriched["security_knowledge"] = knowledge

                # AI Analysis
                enriched["ai_analysis"] = analyze_alert(
                    enriched
                )

                # Response Plan
                enriched["response_plan"] = create_response(
                    enriched
                )

                enriched_alerts.append(enriched)

                logger.info(
                    "Alert processed | threat=%s | risk=%s",
                    enriched.get("threat"),
                    enriched.get("risk_score")
                )

            except Exception as error:

                logger.exception(
                    "Alert processing failed | threat=%s | error=%s",
                    alert.get("threat"),
                    error
                )

                # Keep the original alert so one
                # failed alert does not stop the pipeline.
                failed_alert = alert.copy()

                failed_alert["processing_status"] = "FAILED"
                failed_alert["processing_error"] = str(error)

                enriched_alerts.append(failed_alert)

        # -----------------------------
        # Investigation
        # -----------------------------

        try:

            investigation = investigate(
                enriched_alerts
            )

            logger.info(
                "Investigation completed"
            )

        except Exception as error:

            logger.exception(
                "Investigation failed: %s",
                error
            )

            investigation = {
                "status": "FAILED",
                "error": str(error)
            }

        # -----------------------------
        # Create incident
        # -----------------------------

        incident = {
            "alerts": enriched_alerts,
            "investigation": investigation,
            "status": "OPEN"
        }

        # -----------------------------
        # Store incident
        # -----------------------------

        try:

            saved_incident = save_incident(
                incident
            )

            logger.info(
                "Incident stored | id=%s",
                saved_incident.get("incident_id")
            )

        except Exception as error:

            logger.exception(
                "Incident storage failed: %s",
                error
            )

            return {
                "alerts": enriched_alerts,
                "investigation": investigation,
                "status": "STORAGE_FAILED",
                "error": str(error)
            }

        logger.info(
            "SOC pipeline completed | incident=%s",
            saved_incident.get("incident_id")
        )

        return saved_incident