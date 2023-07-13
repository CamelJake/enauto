import requests
import yaml


BASE_URL = "https://10.10.20.48/restconf"

def main():
    requests.packages.urllib3.disable_warnings()
    #Interface path to get interfaces
    interface_path = "/data/ietf-interfaces:interfaces"
    post_headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json, application/yang-data.errors+json",
    }

    auth = ("developer", "C1sco12345")
    with open(r'C:\Users\xxenc\OneDrive\Documents\enauto_coding\venv\enauto\Python\interfacedata.yml', "r") as handle:
        config_state = yaml.safe_load(handle)
    response = requests.post(
        BASE_URL + interface_path,
        headers=post_headers,
        json=config_state,
        auth=auth,
        verify=False
    )
    if response.status_code == 201:
        print(f"Added interface successfully")
    elif response.status_code == 409:
        print(f"Interface already exists!")
    else:
        print(f"Unexpected {response.status_code}")

if __name__ == "__main__":
    main()