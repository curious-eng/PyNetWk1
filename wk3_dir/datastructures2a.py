
username = 'fictional'
password = 'nosey'
device_list = [
{
    'device_name': 'cisco3',
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
}, {
    'device_name': 'cisco4',
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
}, {
    'device_name': 'arista1',
    'device_type': 'arista_eos',
    'host': 'arista1.lasthop.io',
}, {
    'device_name': 'arista2',
    'device_type': 'arista_eos',
    'host': 'arista2.lasthop.io',
}, {
    'device_name': 'arista3',
    'device_type': 'arista_eos',
    'host': 'arista3.lasthop.io',
}, {
    'device_name': 'arista4',
    'device_type': 'arista_eos',
    'host': 'arista4.lasthop.io',
}, {
    'device_name': 'srx2',
    'device_type': 'juniper_junos',
    'host': 'srx2.lasthop.io',
}, {
    'device_name': 'nxos1',
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
}, {
    'device_name': 'nxos2',
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
},
]
for dev in device_list:
    dev['username'] = username
    dev['password'] = password

