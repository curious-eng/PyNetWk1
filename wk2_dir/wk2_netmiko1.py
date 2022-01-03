from netmiko import ConnectHandler

cisco4 = {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}
net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command_timing('ping', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('8.8.8.8', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
output += net_connect.send_command_timing('', strip_prompt = False, strip_command = False)
print(output)
