from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_vars = {
    "vrf_name": "blue",
    "rd": "100:1",
    "ipv4_enabled": False,
    "ipv6_enabled": True,
}
template_file = "ex3_vrf_template.j2"
template = env.get_template(template_file)
output = template.render(**vrf_vars)
print(output)

