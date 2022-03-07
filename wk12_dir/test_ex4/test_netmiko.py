import os
from netmiko import ConnectHandler
from getpass import getpass
from my_devices import network_devices

def main():
    print(my_connect())

def my_connect():
    device = network_devices[0]
    net_connect = ConnectHandler(**device)
    output = net_connect.find_prompt()
    print(output)
    return net_connect

if __name__ == '__main__':
    main()

def test_find_prompt():
    my_test = my_connect()
    assert my_test.find_prompt() == 'arista1#'

def test_show_version():
    my_test = my_connect()
    a = my_test.send_command('show version')
    print(a)
    assert '4.20.10M' in a
