from meraki_helper import CiscoMeraki
import requests
import json

def main():
    token=""
    meraki = CiscoMeraki(token)
    meraki.get_organization_networks
    meraki.get_organizations
    org_id=""
    body={
        "name": "Test network - Jacob",
        "productTypes": ["appliance", "switch", "camera", "wireless"],
        "timeZone": "America/New_York",
        "tags": ["ENAUTO"],
        "notes": "Test network created by Meraki API",
    }
    meraki.create_organization_network(body, org_id)

if __name__ == "__main__":
    main()