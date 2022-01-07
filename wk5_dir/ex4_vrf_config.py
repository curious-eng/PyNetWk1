from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_vars = {"vrf_list": [{
    "vrf_name": "red",
    "rd": "100:5",
    "ipv4_enabled": False, 
    "ipv6_enabled": True,
}, {
    "vrf_name": "orange",
    "rd": "100:4",
    "ipv4_enabled": True,
    "ipv6_enabled": False,
}, {
    "vrf_name": "yellow",
    "rd": "100:3",
    "ipv4_enabled": True,
    "ipv6_enabled": True,
}, {
    "vrf_name": "green",
    "rd": "100:2",
    "ipv4_enabled": False,
    "ipv6_enabled": False,
}, {
    "vrf_name": "blue",
    "rd": "100:1",
    "ipv4_enabled": True,
    "ipv6_enabled": True,
}]}

template_file = "ex4_vrf_template.j2"
template = env.get_template(template_file)
output = template.render(**vrf_vars)
print(output)

