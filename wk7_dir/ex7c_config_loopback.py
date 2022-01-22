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

cfg_cmds = [
    "interface loopback 167",
    "description JB loopback1",
    "interface loopback 176",
    "description JB loopback2",
]

output = device.config_list(cfg_cmds)

pprint(output)
#my_list = output.findall(".//{*}interface")
#for i in my_list:
#    print(i.text)

