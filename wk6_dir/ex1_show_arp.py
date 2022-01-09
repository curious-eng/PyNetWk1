import pyeapi
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# enable = getpass("Enable: ")
# device = pyeapi.client.Node(connection. enablepwd=enable)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
print(output)
#pprint(output[0]['result']['ipV4Neighbors'][5])

for ip in output[0]['result']['ipV4Neighbors']:
    print(ip['address'] + ' --> ' + ip['hwAddress'])

#{'address': '10.220.88.38',
# 'age': 0,
# 'hwAddress': '0002.00ff.0001',
# 'interface': 'Vlan1, not learned'}

