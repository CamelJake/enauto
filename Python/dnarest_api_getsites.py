#used to get sites, buildings and floors from a DNAC instance

import json
import requests
from requests.exceptions import HTTPError
from dnarest_constants import BASE_URL
import dna_token


def get_all_sites(token):
    token = dna_token.get_token()
    headers = {"X-Auth-Token": token, "Accept": "application/json"}
    resource = "/dna/intent/api/v1/site"
    response = requests.get(BASE_URL + resource, headers=headers, verify=False).json()
    with open(r"C:\Users\xxenc\OneDrive\Documents\enauto_coding\venv\enauto\site_data.json", "w") as sites:
        json.dump(response,sites, indent=2)

def get_single_site(site_name, token):
    token = dna_token.get_token()
    headers = {"X-Auth-Token": token, "Accept": "application/json"}
    resource = f"/dna/intent/api/v1/site?name=Global/{site_name}"
    try:
        response = requests.get(BASE_URL + resource, headers=headers, verify=False).json()
        print(response["response"])
    except HTTPError as err:
        print(f"Encountered HTTP Error: {err}")
    except Exception as exc:
        print(f"Encountered non-HTTP exception: {exc}")
def get_single_building(site_name, building_name,token):
    headers = {"X-Auth-Token": token, "Accept": "application/json"}
    resource = f"/dna/intent/api/v1/site?name=Global/{site_name}/{building_name}"
    try:
        response = requests.get(BASE_URL + resource, headers=headers, verify=False).json()
        print(response["response"])
    except HTTPError as err:
        print(f"Encountered HTTP Error: {err}")
    except Exception as exc:
        print(f"Encountered non-HTTP exception: {exc}")


def main():
    site = "Branch1"
    building = "Building01"
    token=dna_token.get_token()
    #get_all_sites(token)
    #get_single_site(site,token)
    get_single_building(site, building, token)

if __name__ == "__main__":
    main()
