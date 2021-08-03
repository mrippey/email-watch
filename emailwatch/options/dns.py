from emailwatch.secrets import riskiq_username, riskiq_key
import json 
import requests 
from rich import print


auth = (riskiq_username, riskiq_key)
base_riskiq_api_url = "https://api.passivetotal.org/v2/dns/passive"


def get_dns_resolutions(domain):
    

    data = {"compact_record": True, "query": domain}

    try:

        api_response = requests.get(base_riskiq_api_url, auth=auth, json=data)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    dns_resolve = json.loads(api_response.text)

    for resolve in dns_resolve["results"]:
        print(f"[yellow] Resolution: {resolve['resolve']}[/]")
