from netmiko import Netmiko
from yaml import safe_load

def main():
    device = {
        "host":"sandbox-iosxe-latest-1.cisco.com",
        "username":"admin",
        "password" : "C1sco12345",
        "device_type" : "cisco_ios",
    }
    net_conn = Netmiko(**device)
    config = ["interface loopback69", "desc Test loopback"]
    net_conn.send_config_set(config)
    output = net_conn.send_command("show run int loopback69")
    net_conn.save_config()


    print(output)
if __name__ == "__main__":
    main()

    