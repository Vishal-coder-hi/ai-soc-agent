from analyzer.log_parser import analyze_logs
from analyzer.ai_analyst import analyze_alert
from analyzer.investigation_agent import build_investigation
from analyzer.threat_intel import lookup_ip
from analyzer.risk_scorer import calculate_risk
from analyzer.rag_engine import retrieve_knowledge
from analyzer.response_agent import generate_response

LOG_FILE = "logs/security.log"


def main():

    # Step 1: Analyze security logs
    alerts = analyze_logs(LOG_FILE)

    print("\n===== AI SOC AGENT =====\n")

    if not alerts:
        print("✅ No suspicious activity detected.")
        return

    print(f"⚠️ {len(alerts)} security alert(s) detected.\n")

    # Step 2: Display individual alerts + AI analysis
    for number, alert in enumerate(alerts, start=1):

        print(f"ALERT #{number}")

        if "ip" in alert:
            print(f"IP Address: {alert['ip']}")

        if "failed_attempts" in alert:
            print(f"Failed Attempts: {alert['failed_attempts']}")

        print(f"Threat: {alert['threat']}")
        print(f"Severity: {alert['severity']}")
        print(f"Description: {alert['description']}")

                # Threat Intelligence
        enriched_alert = alert.copy()

        if "ip" in alert:
            threat_intel = lookup_ip(alert["ip"])
            enriched_alert["threat_intelligence"] = threat_intel

            print("\n🌐 THREAT INTELLIGENCE")
            print("-" * 50)
            print(threat_intel)

        print("\n🤖 AI SOC ANALYSIS")
        print("-" * 50)

        analysis = analyze_alert(enriched_alert)
        print(analysis)

        print("\n🤖 AI SOC ANALYSIS")
        print("-" * 50)


        risk = calculate_risk(enriched_alert)
                # Security RAG
        knowledge = retrieve_knowledge(enriched_alert)

        enriched_alert["security_knowledge"] = knowledge

        print("\n📚 SECURITY RAG")
        print("-" * 50)

        for item in knowledge:
            print(f"Knowledge Source: {item['file']}")
            print(f"Relevance Score: {item['score']}")
            print("-" * 50)

        enriched_alert["risk_score"] = risk["risk_score"]
        enriched_alert["risk_level"] = risk["risk_level"]

        print("\n🎯 RISK SCORE")
        print("-" * 50)
        print(f"Risk Score: {risk['risk_score']}/100")
        print(f"Risk Level: {risk['risk_level']}")

        analysis = analyze_alert(enriched_alert)
        
        print(analysis)
        print("\n🛡️ SOC RESPONSE PLAN")
        print("=" * 60)

        response_plan = generate_response(enriched_alert)

        print(response_plan)

          
    # Step 3: Build overall investigation
    investigation = build_investigation(alerts)

    print("\n🔎 AI INVESTIGATION SUMMARY")
    print("=" * 60)

    print(f"Total Alerts: {investigation['total_alerts']}")

    print(
        f"High Severity Alerts: "
        f"{len(investigation['high_severity'])}"
    )

    print(
        f"Medium Severity Alerts: "
        f"{len(investigation['medium_severity'])}"
    )

    print("\nPossible Attack Chain:")

    for step in investigation["possible_attack_chain"]:
        print(f"→ {step}")

    # Step 4: AI Incident Investigation
    print("\n🤖 AI INCIDENT INVESTIGATION")
    print("=" * 60)

    print(investigation["ai_report"])


if __name__ == "__main__":
    main()