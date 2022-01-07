from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])

nxos1 = {
    "sw_name": "nxos1",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.1",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.2",
}
nxos2 = {
    "sw_name": "nxos2",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.2",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.1",
}
my_list = [nxos1, nxos2]
output = ""

template_file = 'ex2b_nexux_config.j2'
template = env.get_template(template_file)

for lan_switch in my_list:
    output += lan_switch["sw_name"]
    output += template.render(**lan_switch)

print(output)

