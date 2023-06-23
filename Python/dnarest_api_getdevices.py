import requests
import urllib3 
from dna_token import get_token
from dnarest_constants import BASE_URL

def get_devices(token):
    devices_url = "/dna/intent/api/v1/network-device"
    headers = { 'X-Auth-Token': token, 'Content-Type': 'application/json' }
    urllib3.disable_warnings()
    response = requests.get(BASE_URL + devices_url, headers = headers, verify = False)
    for device in response.json()['response']:
        output = "Hostname:{}, Device ID: {}, Management IP: {}".format(device['hostname'], device['id'], device['managementIpAddress'])
        print(output)

def main():
    token = get_token()
    get_devices(token)
    
if __name__ == '__main__':
    main()
