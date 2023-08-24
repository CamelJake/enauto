import requests
import urllib3
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
from dnarest_constants import BASE_URL

def get_token():
    urllib3.disable_warnings()
    auth_url = "/dna/system/api/v1/auth/token"
    username = "admin"
    password = "Cisco1234!"
    try:
        response = requests.post(BASE_URL + auth_url, auth=HTTPBasicAuth(username, password), verify=False)
        token = response.json()["Token"]
    except HTTPError as http_err:
        print(f"HTTP error occurd: {http_err}")
    else:
        return token
