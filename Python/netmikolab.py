from netmiko import Netmiko
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader

def main():
    #Define Jinja 2 environment. Load templates from my C: drive
    environment = Environment(loader=FileSystemLoader("C:/Users/xxenc/OneDrive/Documents/enauto_coding/venv/enauto/Python/Templates/"))
    #Load in the commands template from the template folder
    template = environment.get_template("commands.txt")
    #Open the Yaml file which contains hosts
    with open(r'C:\Users\xxenc\OneDrive\Documents\enauto_coding\venv\enauto\Python\device.yml', 'r') as file:
        devices = safe_load(file)
    for device in devices["hosts"]:
        net_conn = Netmiko(
            host=device["host"],
            username=device["username"],
            password=device["password"],
            device_type=device["device_type"],
        )
        #Render the tempalte based on device type. The type of command run depends on the device type.
        commands = template.render(device_type = device["device_type"])
        output = net_conn.send_command(commands)
        print(output)
if __name__ == "__main__":
    main()

    