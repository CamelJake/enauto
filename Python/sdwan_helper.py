#Simple SDK used to interact with Cisco SD-WAN API
#Created 8/28/2023 by Jacob Bennett

import json
import requests
from requests.exceptions import HTTPError

class CiscoSDWAN:

    def __init__(self, host, username, password, verify=False):
        #Define object
        self.base_url=f"https://{host}"
        self.verify=verify
        if not self.verify:
            requests.packages.urllib3.disable_warnings()

        #Create SD-WAN Session
        self.session=requests.session()
        auth_response = self.session.post(
            f"{self.base_url}/j_security_check",
            headers={"Content-Type":"application/x-www-form-urlencoded"},
            data={"j_username": username, "j_password": password},
            verify=self.verify
        )
        if auth_response.text:
            auth_response.status_code=401
            auth_response.reason = "UNAUTHORIZED; check username/password"
            auth_response.raise_for_status()
        
        self.headers = {"Accept": "application/json", "Content-Type":"application/json"}

        #Gather XSRF token
        self.xsrf_token=self.session.get(f"{self.base_url}/dataservice/client/token", headers=self.headers, verify=self.verify)





    def get_instance_always_on():
        #Creates a session with the always on Cisco Sandbox
        return CiscoSDWAN(host="sandbox-sdwan-2.cisco.com",
                          username="devnetuser",
                          password="RG!_Yw919_83",
                          )
    
    def _req(self, resource, method="get", params=None, body=None):
        #Used to make various HTTP requests and raise errors
        response = self.session.request(method=method, url=f"{self.base_url}/{resource}",
                                        headers=self.headers,
                                        params=params,
                                        json=body,
                                        verify=self.verify,
                                        )
        response.raise_for_status()
        print(json.dumps(response.json(), indent=2))
        return response
    

    def get_alarm_count(self):
        path="dataservice/alarms/count"
        return self._req(path)


    def get_control_status(self, model=None):
        path="dataservice/device/control/count"
        params={"devce-model": model} if model else None
        return self._req(path)
    

    #Certificates#
    def get_certificate_summary(self):
        path="dataservice/certificate/stats/summary"
        print("----Certificate Summary----")
        return self._req(path)


    def get_controller_certs(self):
        path="dataservice/certificate/vsmart/list"
        print("----VSmart Certs----")
        return self._req(path)


    def get_root_cert(self):
        path="dataservice/certificate/rootcertificate"
        print("----Root Certificate----")
        return self._req(path)


    #Real-Time Statsitics
    #Transport tunnel stats
    def get_tunnel_stats(self, deviceId):
        path="dataservice/device/tunnel/statistics"
        print("----Tunnel Statistics----")
        return self._req(path, params={"deviceId": deviceId})

    #Control conneciton status information. 
    def get_control_count(self, deviceId):
        #Get count of control status of vsmarts and vedges
        path="dataservice/device/control/count"
        print("----Control Connection Info----")
        return self._req(path, params={"deviceId": deviceId})
    
    def get_control_connections(self, deviceId):
        #Get connections list from a device (realtime)
        path="dataservice/device/control/connections"
        print("----Control Connection Info----")
        return self._req(path, params={"deviceId": deviceId})
    

    def get_feature_templates(self):
        path="dataservice/template/feature"
        print("---Feature Templates---")
        return self._req(path)
    
    
    def create_device_template(self):
        #Adds factory default templates to a device template
        all_temps = self.get_feature_templates()
        #filter out the factory default vsmart feature templates
        fd_temps=[]
        for temp in all_temps.json()["data"]:
            temp_type = temp["templateType"].lower()
            if temp["factoryDefault"] and temp_type.endswith("vsmart"):
                fd_temps.append(
                    {
                    "templateId" : temp["templateId"],
                    "templateType": temp["templateType"]
                    }
                )
        print(fd_temps)
        body = {
            "name": "Test Device Template",
            "desc": "Jacobs Test Tempalte. Contains default feature templates",
            "deviceType": "vsmart",
            "configType": "template",
            "policyId": "",
            "featureTemplateUidRange": [],
            "factoryDefault": False,
            "generalTemplates": fd_temps,

        }

        return self._req(resource="dataservice/template/device/feature", method="POST", json=body)
    
    def attach_device_template(self, templateId, var_map):
        
        targetDevices = self.get_devices(deviceType="vsmart")
        print(targetDevices)
        templates=[]
        # Iterate over collected vSmarts
        for dev in targetDevices.json()["data"]:

            # Unpack the var_map and assemble the vSmart dict
            site_id, def_gway = var_map[dev["host-name"]]
            vsmart_dict = {
                "csv-status": "complete",
                "csv-deviceId": dev["uuid"],
                "csv-deviceIP": dev["system-ip"],
                "csv-host-name": dev["host-name"],
                "/0/vpn-instance/ip/route/0.0.0.0/0/next-hop/address": def_gway,
                "//system/host-name": dev["host-name"],
                "//system/system-ip": dev["system-ip"],
                "//system/site-id": site_id,
                "csv-templateId": templateId,
            }
            templates.append(vsmart_dict)
        body = {
            "deviceTemplateList": [
                {
                    "templateId": templateId,
                    "device": templates,
                    "isEdited": False,
                    "isMasterEdited": False,
                }
            ]
        }
        return self._req(resource="dataservice/template/device/config/attachfeature", method="POST", json=body)
    
    def get_devices(self, deviceType):
        return self._req("dataservice/device", params={"device-type":deviceType})

    def define_policy_objects(self, obj_type, name, entries):
        path = f"dataservice/template/policy/list/{obj_type}"
        body={
            "name" : name,
            "description" : "test subscription",
            "type" : obj_type,
            "entries" : entries
        }
        return self._req(path, json=body, method="post")
    

    def get_policy_vsmart(self):
        return self._req(resource="dataservice/template/policy/vsmart")
    

    def get_users(self):
        return self._req(resource="dataservice/admin/user")
    
    def create_user(self, username, password, groups):
        body={
            "groups": groups,
            "username": username,
            "password": password,
            "description": "test",

        }
        return self._req(resource="dataservice/admin/user", method="post", json=body)
    
    def create_usergroup(self, body):
        #User must pass in a json body that will define the group. Returns groupId
        return self._req("dataservice/admin/usergroup", method="post", json=body)

    



        
    




    

    



