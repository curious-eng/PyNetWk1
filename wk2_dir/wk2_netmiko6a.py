from netmiko import ConnectHandler
import time
from pprint import pprint
from getpass import getpass

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
print('prompt is: ' + net_connect.find_prompt())
net_connect.config_mode()
print('now in config mode, prompt is: ' + net_connect.find_prompt())
net_connect.exit_config_mode()
print('exited config mode, prompt is: ' + net_connect.find_prompt())
net_connect.write_channel('disable\n')
print('"disable" sent, prompt is: ' + net_connect.find_prompt())
time.sleep(2)
print('waited 2 seconds, read channel: ' + net_connect.read_channel())
net_connect.enable()
print('entered enable mode, prompt is: ' + net_connect.find_prompt())

