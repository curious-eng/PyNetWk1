from netmiko import ConnectHandler
import time

nxos2 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': '22',
  'global_delay_factor': 2,
}
startTime1 = time.time()
print (time.strftime('%m/%d/%Y %H:%M:%S'))
net_connect = ConnectHandler(**nxos2)
output = net_connect.send_command('show lldp neighbors detail')
print(output)
startTime2 = time.time()
print (time.strftime('%m/%d/%Y %H:%M:%S'))
net_connect = ConnectHandler(**nxos2)
output = net_connect.send_command('show lldp neighbors detail', delay_factor = 8)
print(output)
startTime3 = time.time()
print (time.strftime('%m/%d/%Y %H:%M:%S'))

executionTime = (startTime2 - startTime1)
print('Execution time with global delay = 2: ' + str(executionTime) + ' seconds')

executionTime = (startTime3 - startTime2)
print('Execution time with delay factor = 8: ' + str(executionTime) + ' seconds')

