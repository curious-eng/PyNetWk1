from netmiko import ConnectHandler
import time
from pprint import pprint
import yaml
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

############ define new config #############
nxos1_new_conf = {
    "sw_name": "nxos1",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.1",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.2",
}
nxos2_new_conf = {
    "sw_name": "nxos2",
    "interface": "Ethernet1/1",
    "ip_addr": "10.1.100.2",
    "netmask": 24,
    "as_no": 22,
    "neighbor_ip": "10.1.100.1",
}
############ get device login creds ############
with open('/home/jbrooker/.netmiko.yml', 'r') as f:
    devices = yaml.safe_load(f)
devices['nxos1']['session_log'] = 'nxos1_log.log'#allow easy check of what just happened
devices['nxos2']['session_log'] = 'nxos2_log.log'#allow easy check of what just happened
########### select a subset of devices to update ########### (probably should derive from new_conf somehow)
my_devices = [nxos1_new_conf, nxos2_new_conf]

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
