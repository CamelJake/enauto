import time
import dna_token
from dnarest_constants import BASE_URL
import requests
from requests.exceptions import HTTPError
import json


def wait_for_task(task_id, wait_time=15, attempts=3, token=dna_token.get_token()):
    """
    Waits the wait_time times the number of attempts for the specified
    task_id to be complete. Raises ValueError if the task fails or
    TimeoutError if it fails to complete in the required timeframe.
    """

    time.sleep(wait_time)
    # Query DNA center for the status of the specific task ID
    task_resp = requests.get(BASE_URL+f"/dna/intent/api/v1/task/{task_id}", headers={"X-Auth-Token":token, "Content-Type":"application/json"}, verify=False)
    return task_resp


    

def get_global_credentials(token):
    cred_list = []
    cred_types = ["CLI", "SNMPV2_READ_COMMUNITY", "SNMPV2_WRITE_COMMUNITY"]
    for cred in cred_types:
        creds = requests.get(BASE_URL+"/dna/intent/api/v1/global-credential",headers={"X-Auth-Token":token, "Content-Type":"application/json"},params={"credentialSubType": cred},verify=False)
        cred_Id = creds.json()["response"][0]["id"]
        cred_list.append(cred_Id)
        print(f"Collected credential {cred} with ID {cred_Id}")
    return cred_list

def start_discovery_ipRange(token, timeout=600):
    headers={"X-Auth-Token": token, "Content-Type": "application/json"}
    resource = "/dna/intent/api/v1/discovery"
    with open(r"C:\Users\xxenc\OneDrive\Documents\enauto_coding\venv\enauto\discovery_body.json", "r") as handle:
        body = json.load(handle)
    response = requests.post(BASE_URL+resource, headers=headers, json=body, verify=False)
    #fetch discvovery ID
    print(response.json())
    taskId = response.json()["response"]["taskId"]
    #Wait for response
    print("Gathering Discovey ID")
    discoveryStatus = wait_for_task(taskId)
    discoveryId = discoveryStatus.json()["response"]["progress"]
    success = False
    print("Waiting for discovery to finish")
    for i in range(timeout // 10):
        statusCheck = requests.get(BASE_URL+f"/dna/intent/api/v1/discovery/{discoveryId}", headers=headers, verify=False)
        if statusCheck.json()["response"]["discoveryCondition"].lower() != "complete":
            print(f"Discovery with ID {id} progress status is {statusCheck.json()['response']['discoveryCondition']} {i} ")
        else: 
            print(f"Discovery {discoveryId} completed with this number of devices found: {statusCheck.json()['response']['numDevices']}")
            success=True
            break
    if not success:
        "Discovery timed out"
    discoveredDevices = requests.get(BASE_URL+f"/dna/intent/api/v1/discovery/{discoveryId}/network-device", headers=headers, verify=False)
    print(discoveredDevices.text)



def main():
    diameter = 2
    token = dna_token.get_token()
    start_discovery_ipRange(token)
    #start_discovery_CDP(token, seedIP, diameter)


if __name__ == "__main__":
    main()