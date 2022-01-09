import yaml
from getpass import getpass
import pyeapi

with open("ex2a_arista4.yml", "r") as f:#this is the device details needed for login.
    arista = yaml.safe_load(f)

arista['password'] = getpass()
# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection. enablepwd=enable)

connection = pyeapi.client.connect(**arista)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
#print(output)

for ip in output[0]['result']['ipV4Neighbors']:
    print(ip['address'] + ' --> ' + ip['hwAddress'])

