from dna_token import get_token
from dnarest_api_getdevices import get_devices
import requests
import urllib3
import json
from dnarest_constants import BASE_URL


def add_device(token):
    url = "/dna/intent/api/v1/network-device"
    headers = { 'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
    payload =  {
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }
    json_payload = json.dumps(payload, indent=4)
    response = requests.post(BASE_URL + url, headers = headers, data=json_payload, verify=False)
    print(response)
def main():
    token = get_token()
    add_device(token)
    get_devices(token)
if __name__ == '__main__':
    main()

            
