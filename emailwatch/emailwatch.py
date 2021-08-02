import requests
from secrets import APIKEY
import json
from prompt_toolkit import prompt
from rich import print


base_url = "https://reverse-whois.whoisxmlapi.com/api/v2"
headers = {"Content-Type": "application/json", "Accept": "application/json"}


def get_email_address() -> None:
    enter_email_address = prompt("1 [Email Address]: ")
    print()
    connect_whoisxml_api(enter_email_address)


def connect_whoisxml_api(enter_email_address) -> None:

    data = {
        "basicSearchTerms": {
            "include": [enter_email_address],
        },
        "searchType": "current",
        "mode": "purchase",
        "apiKey": APIKEY,
        "responseFormat": "json",
    }

    try:
        response = requests.post(base_url, data=json.dumps(data), headers=headers)
        response_status_code = response.status_code

        if response_status_code == 200:

            retrieve_whoisxml_results(response)

        else:
            print("[red] Connection not established, try again [/]")

    except requests.ConnectionError:
        return print("[red] Connection error, check the URL and try again")


def retrieve_whoisxml_results(response):

    get_json_from_api = response.json()
    only_return_domains = get_json_from_api["domainsList"]

    for idx, domains in enumerate(only_return_domains):
        print(f"{idx}. {domains}")


def menu():
    print(
        """
  _____                _ _ _    _       _       _     
|  ___|              (_) | |  | |     | |     | |    
| |__ _ __ ___   __ _ _| | |  | | __ _| |_ ___| |__  
|  __| '_ ` _ \ / _` | | | |/\| |/ _` | __/ __| '_ \ 
| |__| | | | | | (_| | | \  /\  / (_| | || (__| | | |
\____/_| |_| |_|\__,_|_|_|\/  \/ \__,_|\__\___|_| |_|
v0.1.0
Discover domains registered by specific email address
Twitter: @nahamike01                                                   
                                                       
    """
    )


def main():
    menu()
    get_email_address()


main()
