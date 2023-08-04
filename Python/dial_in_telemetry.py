import xmltodict
from ncclient import manager
from lxml.etree import fromstring



def main():
    connection_params={
        "host": "10.10.20.48",
        "port": 830,
        "username": "developer",
        "password": "C1sco12345",
        "hostkey_verify": False
    }
    
    with manager.connect(**connection_params) as conn:
        path="/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds"
        sub_response=telemetry_subscribe(conn, path)
        sub_json = xmltodict.parse(sub_response.xml)
        sub_result = sub_json["rpc-reply"]["subscription-result"]["#text"]
        if "ok" in sub_result.lower():
            # Success text: "notif-bis:ok". Print subscription ID also
            sub_id = sub_json["rpc-reply"]["subscription-id"]["#text"]
            print(f"Subscribed to '{path}' via ID: {sub_id}")
        else:
            # Example of an error: "notif-bis:error-no-such-option"
            print(f"Could not subscribe to '{path}'. Reason: {sub_result}")

def telemetry_subscribe(connection, path, period=1000):
    xmlns = "urn:ietf:params:xml:ns:yang:ietf-event-notifications"
    xmlns_yp= "urn:ietf:params:xml:ns:yang:ietf-yang-push"
    subscribe_rpc = f"""
        <establish-subscription xmlns="{xmlns}" xmlns:yp="{xmlns_yp}">
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{path}</yp:xpath-filter>
            <yp:period>{period}</yp:period>
        </establish-subscription>
    """
    susbscribe_resp=connection.dispatch(fromstring(subscribe_rpc))
    return susbscribe_resp

if __name__ == "__main__":
    main()
