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
        resource=f"organizations/{org_id}/networks"
        print(body)
        return self._req(resource, method="post", jsonbody=body)
    
    def update_organization_network(self, net_id):
        resource=f"networks/{net_id}"
        body={
            "name": "CCNP TORTURE CHAMBER",
            "notes": "Updated network with update_organization_network method",
            "productTypes": ["appliance", "switch", "camera", "wireless"],
            "tags": ["ENAUTO", "YEET"],
        }
        return self._req(resource, method="put", jsonbody=body)
    

    def claim_network_devices(self, serials, net_id):
        resource=f"networks/{net_id}/devices/claim"
        body={
            "serials":serials,
        }
        return self._req(resource, method="post", jsonbody=body)
    

    def remove_network_device(self, serials, net_id):
        resource=f"networks/{net_id}/devices/remove"
        for sn in serials:
            body={
                "serial": sn,
            }
            return self._req(resource, method="post", jsonbody=body)


    def update_network_device(self, serial):
        resource=f"devices/{serial}"
        body={
            "name": "TEST NAME",
            "lat": 37.4180951010362,
            "lng": -122.098531723022,
            "serial": serial,
            "tags": [ "recently-added" ]
        }
        return self._req(resource, method="put", jsonbody=body)
    
    def create_webook(self, net_id, url):
        resource=f"networks/{net_id}/webhooks/httpServers"
        body={
            "name": "Jacobs Test Webhook",
            "url": url,
        }
        return self._req(resource, method="post", jsonbody=body)
    

    def test_webhook(self, net_id, webhookUrl):
        #Tests webhook with generic power supply down alert. Returns test id)
        resource=f"networks/{net_id}/webhooks/webhookTests"
        body={"url": webhookUrl}
        return self._req(resource, method="post", jsonbody=body)
    

    def get_webhook_test_result(self, net_id, test_id):
        resource=f"networks/{net_id}/webhooks/webhookTests/{test_id}"
        return self._req(resource)


    def get_wireless_ssids(self, net_id):
        return self._req(resource=f"networks/{net_id}/wireless/ssids")
    
    def update_wireless_ssid(self, net_id, ssid_number):
        body={
            "name": "test Update",
            "enabled": False,
            "authMode": "psk",
            "psk": "test123!",
        }
        return self._req(resource=f"networks/{net_id}/wireless/ssids/{ssid_number}", 
                         method="put", 
                         jsonbody=body
                         )
    
    def get_splash_login_attempts(self, net_id, ssid_id):
        return self._req(resource=f"networks/{net_id}/splashLoginAttemps", params={"ssidNumber": ssid_id})
    
    def update_wireless_splash_settings(self, net_id, ssid_id, splashUrl):
        body={
            "splashUrl": splashUrl,
            "useSplashUrl": True,
            "redirectUrl": "https://google.com",
            "useRedirectUrl": True,
        }
        return self._req(resource=f"networks/{net_id}/wireless/ssids/{ssid_id}/splash/settings", method="put", jsonbody=body)
    

    def get_wireless_splash_settings(self, net_id, ssid_id):
        return self._req(resource=f"networks/{net_id}/wireless/ssids/{ssid_id}/splash/settings")
    
    #Cameras

    def get_live_videlink(self, sn):
        return self._req(resource=f"devices/{sn}/camera/videoLink")

    def get_mv_snapshot(self, sn):
        return self._req(resource=f"devices/{sn}/camera/generateSnapshot")
    
    def get_mv_qualitysettings(self, sn):
        return self._req(resource=f"devices/{sn}/camera/qualityAndRetention")

    def get_mv_analytics(self, sn, timeFrame):
        return self._req(resource=f"devices/{sn}/camera/analytics/{timeFrame}")
    
    #Returns historical records for an analytic zone aggregated per minute
    def get_mv_history_zones(self, sn, zoneId):
        return self._req(resource=f"devices/{sn}/camera/analytics/zones/{zoneId}/history")
    
    #Returns all coinfigured analytic zones for a camera
    def get_mv_analytic_zones(self ,sn):
        return self._req(resource=f"devices/{sn}/camera/analytics/zones")



    

