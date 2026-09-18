import os
import ipaddress
import requests
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")

VT_URL = "https://www.virustotal.com/api/v3/ip_addresses/{}"


def lookup_ip(ip):
    """
    Check an IP address using VirusTotal threat intelligence.
    """

    # Check whether the IP is valid
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        return {
            "ip": ip,
            "status": "invalid_ip"
        }

    # Private IPs are not useful for public threat intelligence
    if ip_obj.is_private:
        return {
            "ip": ip,
            "status": "private_ip",
            "message": "Private IP - public threat intelligence lookup skipped."
        }

    # API key check
    if not VT_API_KEY:
        return {
            "ip": ip,
            "status": "api_key_missing"
        }

    try:
        response = requests.get(
            VT_URL.format(ip),
            headers={
                "x-apikey": VT_API_KEY
            },
            timeout=10
        )

        if response.status_code == 404:
            return {
                "ip": ip,
                "status": "not_found"
            }

        response.raise_for_status()

        data = response.json()

        attributes = data["data"]["attributes"]

        stats = attributes.get(
            "last_analysis_stats",
            {}
        )

        return {
            "ip": ip,
            "status": "found",
            "reputation": attributes.get("reputation"),
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
            "undetected": stats.get("undetected", 0),
            "country": attributes.get("country"),
            "as_owner": attributes.get("as_owner")
        }

    except requests.RequestException as error:
        return {
            "ip": ip,
            "status": "lookup_failed",
            "error": str(error)
        }