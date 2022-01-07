from netmiko import ConnectHandler
import time
from pprint import pprint
import yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import json

from password import password
############ load new config from file as a list #############
filename = 'ex2e_nexus_config.json'

with open(filename) as f:
    my_devices = json.loads(f.read())

import sys
sys.exit()
############ get device login creds ############
with open('/home/jbrooker/.netmiko.yml', 'r') as f:
    devices = yaml.safe_load(f)
devices['nxos1']['session_log'] = 'nxos1_log.log'#allow easy check of what just happened
devices['nxos2']['session_log'] = 'nxos2_log.log'#allow easy check of what just happened

########### set-up Jinja2 environment #############
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])

########### generate config from template and login/configure switch ###############

template_file = 'ex2c_nexus_config.j2'
template = env.get_template(template_file)

for lan_switch in my_devices:
    output = template.render(**lan_switch)#'output' is the new config from jinja2 template as string
    net_connect = ConnectHandler(**devices[lan_switch['sw_name']])#this logs into the correct switch
#    print(net_connect.find_prompt())
    net_connect.send_config_set(output.splitlines())#this sends the new config as a list
#    break
#import sys
#sys.exit()

#########################################################
