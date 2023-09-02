import requests
import json

class CiscoMeraki:
    def __init__(self, token):
        #Get token
        self.token = token
        #Set verify
        self.verify=False
        #v0 headers
        #self.headers={"X-Cisco-Meraki-Api-Key": self.token, "Accept": "application/json", "Content-Type":"application/json"}
        #v1 headers
        self.headers={"Authorization": f"Bearer {self.token}", "Accept": "application/json", "Content-Type":"application/json"}
        self.base_url=f"https://api.meraki.com/api/v1"

    def _req(self, resource, method="get", params=None, jsonbody=None):
        response = requests.request(url=f"{self.base_url}/{resource}", 
                                    headers=self.headers, 
                                    verify=self.verify, 
                                    json=jsonbody,
                                    params=params,
                                    method=method,
                                    )
        print(json.dumps(response.json(), indent=2))
        return response
    
    def get_organizations(self):
        return self._req(resource="organizations")
    
    def get_organization_networks(self, org_id):
        return self._req(resource=f"organizations/{org_id}/networks")
    
    def create_organization_network(self, body, org_id):
        resource=f"organization/{org_id}/networks"
        return self._req(resource, method="post", json=body)
    
    def update_organization_network(self, net_id):
        resource=f"networks/{net_id}"
        body={
            "notes": "Updated network with update_organization_network method",
            "tags": ["ENAUTO", "YEET"],
        }
        return self._req(resource, method="put", json=body)
    

    def claim_network_devices(self, serials, net_id):
        resource=f"networks/{net_id}/devices/claim"
        body={
            "serials":serials,
        }
        return self._req(resource, method="post", json=body)
    

    def remove_network_device(self, serials, net_id):
        resource=f"networks/{net_id}/devices/remove"
        for sn in serials:
            body={
                "serial": sn,
            }
            return self._req(resource, method="post", json=body)


    def update_network_device(self, serial):
        resource=f"devices/{serial}"
        body={
            "name": "TEST NAME",
            "lat": 37.4180951010362,
            "lng": -122.098531723022,
            "serial": serial,
            "mac": "00:11:22:33:44:55",
            "tags": [ "recently-added" ]
        }
        return self._req(resource, method="put", json=body)
    
    def create_webook(self, net_id, body):
        resource=f"/networks/{net_id}/webooks/httpservers"
        body={
            "name": "Test Webhook",
            "url": "https://",
            "sharedSecret": "secret",
        }
        return self._req(resource, method="post", json=body)
    

    def test_webhook(self, net_id, webhookUrl):
        #Tests webhook with generic power supply down alert. Returns test id)
        resource=f"/networks/{net_id}/webhooks/webhooktests"
        body={"url": webhookUrl}
        return self._req(resource, method="post", json=body)
    

    def get_webhook_test_result(self, net_id, test_id):
        resource=f"/networks/{net_id}/webhooks/webhooktests/{test_id}"
        return self._req(resource)


    def get_wireless_ssids(self, net_id):
        return self._req(resource=f"/networks/{net_id}/wireless/ssids")
    
    def update_wireless_ssid(self, net_id, ssid_number):
        body={
            "name": "test Update",
            "enabled": False,
            "authMode": "8021x-radius",
            "psk": "test123!",
        }
        return self._req(resource=f"networks/{net_id}/wireless/ssids/{ssid_number}", 
                         method="put", 
                         json=body
                         )
    

