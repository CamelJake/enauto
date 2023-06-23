import requests
import urllib3
from requests.auth import HTTPBasicAuth
from dnarest_constants import BASE_URL

def get_token():
    urllib3.disable_warnings()
    auth_url = "/dna/system/api/v1/auth/token"
    username = "devnetuser"
    password = "Cisco123!"
    response = requests.post(BASE_URL + auth_url, auth=HTTPBasicAuth(username, password), verify=False)
    token = response.json()["Token"]
    return token
