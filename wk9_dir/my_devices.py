#!/usr/bin/env python
from getpass import getpass

pw = getpass()
cisco3_dict = dict(
    hostname='cisco3.lasthop.io',
    device_type='ios',
    username='pyclass',
    password=pw,
    optional_args={},
)

arista1_dict = dict(
    hostname='arista1.lasthop.io',
    device_type='eos',
    username='pyclass',
    password=pw,
    optional_args={},
)

nxos1_dict = dict(
    hostname='nxos1.lasthop.io',
    device_type='nxos',
    username='pyclass',
    password=pw,
    optional_args={'port': 8443},
)

device_dict = dict(
    cisco3=cisco3_dict,
    arista1=arista1_dict,
    nxos1=nxos1_dict,
)

