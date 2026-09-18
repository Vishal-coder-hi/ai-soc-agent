from analyzer.threat_intel import lookup_ip


def enrich_alert(alert):
    """
    Threat Intelligence Agent:
    Enriches alerts with external threat intelligence.
    """

    enriched_alert = alert.copy()

    if "ip" in alert:
        enriched_alert["threat_intelligence"] = lookup_ip(
            alert["ip"]
        )

    return enriched_alert