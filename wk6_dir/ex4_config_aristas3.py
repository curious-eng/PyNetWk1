import yaml
from getpass import getpass
import pyeapi
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

def read_yaml(filename):
    with open(filename, "r") as f:
        return(yaml.safe_load(f))

def write_yaml(filename, config_list):
    with open(filename, "w") as f:
        yaml.dump(config_list, f, default_flow_style=True)

def send_cmd_to_arista(arista, my_command):
    connection = pyeapi.client.connect(**arista)
    device = pyeapi.client.Node(connection)
    return(device.enable(my_command))

def send_config_to_arista(**arista):#dict (key 'data' contains config cmd list)
    connection = pyeapi.client.connect(**arista)
    device = pyeapi.client.Node(connection)
    return(device.config(arista['config']))

def generate_jinja_config(**my_dict):#dict (k,v are vars in jinja template
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader([".", "./templates"])
    #
    template_file = 'ex4_arista_config.j2'
    template = env.get_template(template_file)
    config = template.render(**my_dict)
    return(config)

if __name__=='__main__':
    password = getpass()
    yaml_config = read_yaml('ex4_devices.yml')
    for k, v in yaml_config[0].items():
        arista_config_list = generate_jinja_config(**v['data']).splitlines()
        pprint(arista_config_list)
        v['config'] = arista_config_list
        v['password'] = password
        result_list = send_config_to_arista(**v)
        print(result_list)
        pprint(send_cmd_to_arista(v, 'show ip interface brief'))

