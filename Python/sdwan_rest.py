from sdwan_helper import CiscoSDWAN
import json
import requests


def main():
    sdwan = CiscoSDWAN.get_instance_always_on()
    #sdwan.get_alarm_count()
    #sdwan.get_certificate_summary()
    #sdwan.get_control_connection_info()
    #sdwan.get_controller_certs()
    #sdwan.get_root_cert()
    #sdwan.get_tunnel_stats(deviceId="ed0863cb-83e7-496c-b118-068e2371b13c")
    template_resp = sdwan.create_device_template()
    templateId=template_resp.json()["templateId"]
    #debug, print tempalteId
    #print(templateId)
    activation_resp = sdwan.attach_device_template(templateId, var_map)

if __name__ == "__main__":
    main()