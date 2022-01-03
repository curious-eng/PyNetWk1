from netmiko import ConnectHandler
import time
from pprint import pprint

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
    net_connect = ConnectHandler(**device)
    my_out = net_connect.send_command('show vlan brief', use_textfsm=True)
    pprint(my_out)
    my_cmds = net_connect.send_config_from_file('wk2_netmiko5_commands.txt')
    print(net_connect.find_prompt())
    my_out = net_connect.send_command('show vlan brief', use_textfsm=True)
    pprint(my_out)
    net_connect.disconnect()


