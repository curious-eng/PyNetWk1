from netmiko import ConnectHandler
import time
from pprint import pprint

cisco3 = {
  'device_type': 'cisco_ios',
  'host': 'cisco3.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}
print('before  "net_connect = ConnectHandler(**cisco3)"')
net_connect = ConnectHandler(**cisco3)
print('after  "net_connect = ConnectHandler(**cisco3)"')
#output = net_connect.send_command('ping google.com')
#output = net_connect.send_command('show running-config all', use_textfsm=True)
cmd_list1 = [
    'no ip domain-lookup',
    'no name-server 1.1.1.1',
    'no name-server 1.0.0.1',
]
cmd_list2 = [
    'name-server 1.1.1.1',
    'name-server 1.0.0.1',
    'ip domain-lookup',
]

output1 = net_connect.send_config_set(cmd_list1)
#
ping_out = net_connect.send_command('ping google.com')
print(ping_out)

output2 = net_connect.send_config_set(cmd_list2)
#net_connect.disconnect()
 
ping_out = net_connect.send_command('ping google.com')
print(ping_out)

net_connect.disconnect()
#lines = output.split('\n')
#line0 = ''
#line1 = ''
#line2 = ''
#for line in lines:
#    line2 = line
#    if 'domain-lookup' in line1 or 'name-server' in line1:
#        if 'domain-lookup' in line1:
#            print(line0)
#            print(line1)
#            print(line2)
#        else:
#            print(line1)
#    line0 = line1
#    line1 = line

