from dna_token import get_token
import requests
import urllib3
from dnarest_constants import BASE_URL

def delete_device(token):
    id = 123456
    url = f"/dna/intent/api/v1/network-device/{id}"
    headers = { 'X-Auth-Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json' }
    response = requests.delete(BASE_URL + url, headers=headers, data=None, verify=False )
    if response.ok:
        print(f"Deleted device with id {id} successfully")
        print(response.text.encode('utf8'))
    else: 
        print("Delete failed with the following reason {}".format(response.text.encode('UTF8')))

def main():
    token = get_token()
    delete_device(token)
if __name__ == "__main__":
    main()


    