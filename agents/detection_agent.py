from analyzer.log_parser import analyze_logs


def detect_alerts(log_file):
    """
    Detection Agent:
    Reads security logs and detects suspicious activity.
    """

    alerts = analyze_logs(log_file)

    return alerts