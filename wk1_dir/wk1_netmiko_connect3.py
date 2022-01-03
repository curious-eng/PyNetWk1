from netmiko import ConnectHandler
from getpass import getpass
cisco3 = {
  'device_type': 'cisco_ios',
  'host': 'cisco3.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}
net_connect = ConnectHandler(**cisco3)
with open("cisco3_show_ver.txt", "w") as f:
    f.writelines(net_connect.send_command('show version'))
