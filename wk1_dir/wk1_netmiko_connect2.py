from netmiko import ConnectHandler
from getpass import getpass
nxos1 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos1.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': '22',
}
nxos2 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': '22',
}
my_devices = [nxos1, nxos2]
for device in my_devices:
    #print(device)
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

