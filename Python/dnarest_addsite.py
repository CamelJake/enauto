import json
import requests
from requests.exceptions import HTTPError
from dnarest_constants import BASE_URL
import dna_token
import time


def add_site(token):
    with open(r"C:\Users\xxenc\OneDrive\Documents\enauto_coding\venv\enauto\site.json", "r") as handle:
        data = json.load(handle)
    resource = "/dna/intent/api/v1/site"
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    URL=BASE_URL+resource
    print(f"Adding new site with name {data['site']['area']['name']}")
    try:
        response = requests.post(url=f'{URL}', json=data, headers=headers, verify=False)
    except HTTPError as http_err:
        print(f"HTTP error occured -> {http_err}")
    except Exception as exc:
        print(f"Some other exception occured {exc}")
    else:
        print("Site added, wiating for execution to complete")
        status_resp=get_execution_status(response.json()["executionStatusUrl"])
        if status_resp.json()["status"].lower() != "success":
            raise ValueError(f"Site object addition failed {status_resp.json()['status']}")

def get_execution_status(statusUrl, wait_time=5, token=dna_token.get_token()):
    """
    Local helper function to wait for individual site objects to be created.
    This API is asynchronous and uses HTTP status 202, but does not use the
    same "task ID" query process as most other DNA Center tasks.
    """
    done = False

    # Continue looping while we are not done
    while not done:
        time.sleep(wait_time)

        # After waiting, issue the request and see if the task is in progress
        status_resp = requests.get(BASE_URL+statusUrl, headers={"X-Auth-Token": token, "Content-Type": "application/json"}, verify=False)
        done = status_resp.json()["status"].lower() != "in_progress"
    return status_resp

def main():
    token = dna_token.get_token()
    add_site(token)


if __name__ == "__main__":
    main()