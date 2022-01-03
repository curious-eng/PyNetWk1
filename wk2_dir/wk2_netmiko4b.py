from netmiko import ConnectHandler
import time
from pprint import pprint

cisco3 = {
   'device_type': 'cisco_ios',
   'host': 'cisco3.lasthop.io',
   'username': 'pyclass',
   'password': '88newclass',
}
#print('before  "net_connect = ConnectHandler(**cisco3)"')
net_connect = ConnectHandler(**cisco3)
#print('after  "net_connect = ConnectHandler(**cisco3)"')

cmd_list1 = [
    'no ip domain-lookup',
    'no ip name-server 1.1.1.1',
    'no ip name-server 1.0.0.1',
]
cmd_list2 = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

#output1 = net_connect.send_config_set(cmd_list1)
#print(output1)

ping_out = net_connect.send_command('ping google.com')
print(ping_out)

output2 = net_connect.send_config_set(cmd_list2)
print(output2)

ping_out = net_connect.send_command('ping google.com')
print(ping_out)

net_connect.disconnect()


