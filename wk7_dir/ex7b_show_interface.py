from pprint import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from getpass import getpass

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

cmds = [
    "show system uptime",
    "show system resources",
]

output = device.show_list(cmds)
#print(output)
for i in output:
    pprint(etree.tostring(i).decode())
    print()
#print("Interface: {}; State: {}; MTU: {}".format(output.find(".//{*}interface").text, output.find(".//{*}state").text, output.find(".//{*}eth_mtu").text))

#In [7]: output.find(".//{*}interface").text
#Out[7]: 'Ethernet1/1'
#
#In [8]: output.find(".//{*}state").text
#Out[8]: 'up'
#
#In [9]: output.find(".//{*}eth_mtu").text
#Out[9]: '1500'


