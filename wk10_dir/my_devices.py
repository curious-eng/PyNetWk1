from getpass import getpass

#d = dict([
#    (<key>, <value>),
#    (<key>, <value),
#      .
#      .
#      .
#    (<key>, <value>)
#])

cisco3 = dict([
  ('device_type', 'cisco_ios'),
  ('host', 'cisco3.lasthop.io'),
  ('username', 'pyclass')
])

arista1 = dict([
  ('device_type', 'arista_eos'),
  ('host', 'arista1.lasthop.io'),
  ('username', 'pyclass'),
  ('global_delay_factor', 4)
])

arista2 = dict([
  ('device_type', 'arista_eos'),
  ('host', 'arista2.lasthop.io'),
  ('username', 'pyclass'),
  ('global_delay_factor', 4)
])

srx2 = dict([
  ('device_type', 'juniper_junos'),
  ('host', 'srx2.lasthop.io'),
  ('username', 'pyclass')
])

device_dict = {
    'cisco3': cisco3,
    'arista1': arista1,
    'arista2': arista2,
    'srx2': srx2,
}

password = getpass()
for a in device_dict:
    device_dict[a]['password'] = password

network_devices = [cisco3, arista1, arista2, srx2]

device_list = [cisco3, arista1, arista2, srx2]
