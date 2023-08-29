
import sdwan_helper
import json
import requests


def main():
    baseUrl = "https://sandbox-sdwan-2.cisco.com"
    sdwan_helper.build_session("devnetuser", "RG!_Yw919_83", baseUrl)

if __name__ == "__main__":
    main()