import requests
import urllib3
from requests.auth import HTTPBasicAuth

def get_token():
    urllib3.disable_warnings()
    base_url = "https://sandboxdnac.cisco.com"
    auth_url = "/dna/system/api/v1/auth/token"
    username = "devnetuser"
    password = "Cisco123!"
    response = requests.post(base_url + auth_url, auth=HTTPBasicAuth(username, password), verify=False)
    token = response.json()["Token"]
    return token
