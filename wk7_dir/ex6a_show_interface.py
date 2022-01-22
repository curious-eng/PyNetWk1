import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from getpass import getpass

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
print("Interface: {}; State: {}; MTU: {}".format(output['TABLE_interface']['ROW_interface']['interface'], output['TABLE_interface']['ROW_interface']['state'], output['TABLE_interface']['ROW_interface']['eth_mtu']))

#output['TABLE_interface']['ROW_interface']['interface']
#Out[10]: 'Ethernet1/1'
#
#In [11]: output['TABLE_interface']['ROW_interface']['state']
#Out[11]: 'up'
#
#In [12]: output['TABLE_interface']['ROW_interface']['MTU']
#---------------------------------------------------------------------------
#KeyError                                  Traceback (most recent call last)
#<ipython-input-12-2ed4a555d5f6> in <module>
#----> 1 output['TABLE_interface']['ROW_interface']['MTU']
#
#KeyError: 'MTU'
#
#In [13]:
#
#In [13]: output['TABLE_interface']['ROW_interface']['eth_mtu']
#Out[13]: '1500'


