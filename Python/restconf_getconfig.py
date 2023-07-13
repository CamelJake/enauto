import requests

BASE_URL = "https://10.10.20.48/restconf"

def main():
    requests.packages.urllib3.disable_warnings()
    #Interface path to get interfaces
    interface_path = "/data/ietf-interfaces:interfaces/interface"
    headers = {"Accept": "application/yang-data+json"}
    auth = ("developer", "C1sco12345")
    response = requests.get(
        BASE_URL + interface_path,
        headers=headers,
        auth=auth,
        verify=False
    )
    interfaces = response.json()["ietf-interfaces:interface"]
    for interface in interfaces:
        print(interface)

if __name__ == "__main__":
    main()

