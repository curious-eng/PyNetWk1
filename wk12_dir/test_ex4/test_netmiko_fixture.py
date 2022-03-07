import pytest
import os
from netmiko import ConnectHandler
from getpass import getpass
from my_devices import network_devices

def main():
    print(my_connect())

@pytest.fixture(scope='module')
def my_connect():
    device = network_devices[0]
    net_connect = ConnectHandler(**device)
    output = net_connect.find_prompt()
    print(output)
    return net_connect

if __name__ == '__main__':
    main()

def test_find_prompt(my_connect):
    assert my_connect.find_prompt() == 'arista1#'

def test_show_version(my_connect):
    assert '4.20.10M' in my_connect.send_command('show version')

