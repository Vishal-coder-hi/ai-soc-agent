def calculate_risk(alert):
    """
    Calculate a risk score between 0 and 100
    using alert severity and threat intelligence.
    """

    score = 0

    # -------------------------
    # 1. Base severity score
    # -------------------------

    severity = alert.get("severity", "").upper()

    if severity == "CRITICAL":
        score += 50
    elif severity == "HIGH":
        score += 40
    elif severity == "MEDIUM":
        score += 25
    elif severity == "LOW":
        score += 10

    # -------------------------
    # 2. Threat intelligence
    # -------------------------

    ti = alert.get("threat_intelligence", {})

    malicious = ti.get("malicious", 0)
    suspicious = ti.get("suspicious", 0)

    if isinstance(malicious, int):
        score += min(malicious * 3, 30)

    if isinstance(suspicious, int):
        score += min(suspicious * 2, 10)

    # -------------------------
    # 3. Brute-force attempts
    # -------------------------

    failed_attempts = alert.get("failed_attempts", 0)

    if isinstance(failed_attempts, int):
        if failed_attempts >= 10:
            score += 15
        elif failed_attempts >= 5:
            score += 10
        elif failed_attempts >= 3:
            score += 5

    # -------------------------
    # 4. Cap score at 100
    # -------------------------

    score = min(score, 100)

    # -------------------------
    # 5. Risk level
    # -------------------------

    if score >= 80:
        risk_level = "CRITICAL"
    elif score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "risk_score": score,
        "risk_level": risk_level
    }