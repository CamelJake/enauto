#Simple SDK used to interact with Cisco SD-WAN API
#Created 8/28/2023 by Jacob Bennett

import json
import requests
from requests.exceptions import HTTPError



#Creates SD-WAN session
def build_session(username, password, baseUrl):
    path="/j_security_check"
    body= {"username": username, "password": password}
    headers={"Content-Type": "application/x-www-form-urlencoded"}
    response=requests.post(baseUrl+path, headers=headers, data=body, verify=False)
    print(response.headers)
    try:
        cookies=response.headers["Set-Cookie"]
        jsessionid = cookies.split(";")
        print(f"jession id: {jsessionid}")
        return jsessionid[0]
    except:
        print("Jession ID not found")
def get_alarm_count(jsessionid, baseUrl):
    path="/dataservice/alarms/count"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

def get_control_status(jsessionid, baseUrl):
    path="/dataservice/device/control/count"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

#Certificates#

def get_certificate_summary(jsessionid, baseUrl):
    path="/dataservice/certificate/stats/summary"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

def get_controller_certs(jsessionid, baseUrl):
    path="/dataservice/certificate/vsmart/list"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

def get_root_cert(jsessionid, baseUrl):
    path="/dataservice/certificate/rootcertificate"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

#Real-Time Statsitics
#Transport tunnel stats
def get_tunnel_stats(jsessionid, baseUrl):
    path="/dataservice/device/tunnel/statistics"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")

#Control conneciton status information. 
def get_control_connection_info(jsessionid, baseUrl):
    path="/dataservice/device/control/connections"
    headers={"Cookie": jsessionid, "Content-Type": "application/json"}
    try:
        response = requests.get(baseUrl+path, headers=headers, verify=False)
        print(response)
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as exc:
        print(f"Other exception occured: {exc}")



    

    



