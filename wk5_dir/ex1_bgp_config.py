from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])

my_vars = {
    "local_as": 10,
    "peer1_ip": "10.1.20.2",
    "peer1_as": 20,
    "peer2_ip": "10.1.30.2",
    "peer2_as": 30,
}

template_file = 'ex1_bgp_config.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

