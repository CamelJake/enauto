from meraki_helper import CiscoMeraki
import requests
import json

def main():
    token="34dbf1e204b30c7197b814c4f0f3359db317fade"
    meraki = CiscoMeraki(token)
    #org_id=meraki.get_organizations().json()[0]["id"]
    """
    body={
        "name": "Test network - Jacob",
        "productTypes": ["appliance", "switch", "camera", "wireless"],
        "timeZone": "America/New_York",
        "tags": ["ENAUTO"],
        "notes": "Test network created by Meraki API"
    }
    meraki.create_organization_network(body, org_id)
    """
    jacobs_network = "L_646829496481114937"
    #meraki.update_organization_network(jacobs_network)
    #meraki.update_network_device(serial="Q2JD-CAF3-Y6G2")
    #meraki.create_webook(net_id=jacobs_network, url="https://webhook.site/e9f4a22a-c14f-4477-b909-5c22e40b3bb3")
    #test_id=meraki.test_webhook(net_id=jacobs_network, webhookUrl="https://webhook.site/e9f4a22a-c14f-4477-b909-5c22e40b3bb3").json()["id"]
    #meraki.get_webhook_test_result(jacobs_network,"646829496481585731")
    #meraki.get_wireless_ssids(jacobs_network)
    #meraki.update_wireless_ssid(net_id=jacobs_network, ssid_number=1)
    #meraki.get_splash_login_attempts(jacobs_network, ssid_id=1)
    #meraki.get_wireless_splash_settings(jacobs_network, 1)
    #meraki.get_live_videlink("QBSD-6Z53-VFXL")
    #meraki.get_mv_snapshot("QBSD-6Z53-VFXL")
    #meraki.get_mv_qualitysettings("QBSD-6Z53-VFXL")
    #meraki.get_mv_analytics("QBSD-6Z53-VFXL", "overview")
    #meraki.get_mv_history_zones("QBSD-6Z53-VFXL", 0)
    meraki.get_mv_analytic_zones("QBSD-6Z53-VFXL")
if __name__ == "__main__":
    main()