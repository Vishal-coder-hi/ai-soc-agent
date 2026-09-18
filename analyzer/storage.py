import json
import os


STORAGE_FILE = "storage/results.json"


def load_results():
    """
    Load previously processed SOC results.
    """

    if not os.path.exists(STORAGE_FILE):
        return []

    try:
        with open(STORAGE_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_results(results):
    """
    Save processed SOC results.
    """

    os.makedirs(
        os.path.dirname(STORAGE_FILE),
        exist_ok=True
    )

    with open(STORAGE_FILE, "w") as file:
        json.dump(
            results,
            file,
            indent=4
        )


def find_cached_alert(alert, results):
    """
    Find an already processed alert.
    """

    for stored_alert in results:

        if (
            stored_alert.get("threat") == alert.get("threat")
            and stored_alert.get("ip") == alert.get("ip")
            and stored_alert.get("description") == alert.get("description")
        ):
            return stored_alert

    return None