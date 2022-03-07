import pytest
#import os
from netmiko import ConnectHandler
from getpass import getpass
#from my_devices import network_devices

def test_find_prompt(my_connect):
    assert 'arista1#' in my_connect.find_prompt()

def test_show_version(my_connect):
    assert '4.20.10M' in my_connect.send_command('show version')

