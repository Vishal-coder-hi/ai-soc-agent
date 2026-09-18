from analyzer.response_agent import generate_response


def create_response(alert):
    """
    Response Agent:
    Generates a recommended SOC response plan.
    """

    return generate_response(alert)