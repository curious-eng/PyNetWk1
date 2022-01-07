from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

cisco3_vars = {
    "timezone": "EST",
    "timezone_offset": -5,
    "timezone_dst": 0,
    "ntp_server1": "130.126.24.24",
    "ntp_server2": "152.2.21.1",
}
template_file = "ex5_cisco3_config.j2"
template = env.get_template(template_file)
output = template.render(**cisco3_vars)
print(output)

