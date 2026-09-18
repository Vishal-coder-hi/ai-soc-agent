from analyzer.investigation_agent import build_investigation


def investigate(alerts):
    """
    Investigation Agent:
    Correlates multiple alerts and generates
    an incident investigation.
    """

    return build_investigation(alerts)