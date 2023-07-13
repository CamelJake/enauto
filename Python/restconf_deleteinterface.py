import requests

BASE_URL = "https://10.10.20.48/restconf"

def main():
    requests.packages.urllib3.disable_warnings()

    target_interface="/data/ietf-interfaces:interfaces/interface=Loopback69"
    headers = {"Accept": "application/yang-data+json"}
    auth = ("developer", "C1sco12345")
    response = requests.delete(
        BASE_URL + target_interface,
        auth=auth,
        headers=headers,
        verify=False
    )

    print(response.text)
    if response.status_code == 204:
        print("obj deleted successfully")
    elif response.status_code == 404: print("Object not found or already deleted.")
    else: print(f'Unexpected error occured {response.status_code}')

if __name__=="__main__":
    main()


