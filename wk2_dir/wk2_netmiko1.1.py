from netmiko import ConnectHandler

cisco4 = {
  'device_type': 'cisco_ios',
  'host': 'cisco4.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
}
net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command('ping', expect_string = 'Protocol') + '\n'
output += net_connect.send_command('', expect_string = 'Target IP address') + '\n'
output += net_connect.send_command('8.8.8.8', expect_string = 'Repeat count') + '\n'
output += net_connect.send_command('', expect_string = 'Datagram size') + '\n'
output += net_connect.send_command('', expect_string = 'Timeout in seconds') + '\n'
output += net_connect.send_command('', expect_string = 'Extended commands') + '\n'
output += net_connect.send_command('', expect_string = 'Sweep range of sizes') + '\n'
output += net_connect.send_command('', expect_string = '#') + '\n'
print(output)
