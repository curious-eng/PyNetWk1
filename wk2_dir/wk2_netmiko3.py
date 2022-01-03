from netmiko import ConnectHandler
import time
from pprint import pprint

cisco4 = {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}

net_connect = ConnectHandler(**cisco4)
#output = net_connect.send_command('show lldp neighbors detail')
#output += net_connect.send_command('show version')
#pprint(output)

output1 = net_connect.send_command('show lldp neighbors detail', use_textfsm=True)
output2 = net_connect.send_command('show version', use_textfsm=True)
net_connect.disconnect()
#pprint(output)
print('LLDP neighbour interface:', output1[0]['neighbor_interface']) 
