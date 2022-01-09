def generate_jinja_config(**my_dict):
    from jinja2 import FileSystemLoader, StrictUndefined
    from jinja2.environment import Environment
    from pprint import pprint

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader([".", "./templates"])

#arista1 = {dict "hostname", "intf_name", "intf_ip", "intf_mask"}
#arista2 = {dict "hostname", "intf_name", "intf_ip", "intf_mask"}
#arista3 = {dict "hostname", "intf_name", "intf_ip", "intf_mask"}
#arista4 = {dict "hostname", "intf_name", "intf_ip", "intf_mask"}
#my_list = [arista1, arista2, arista3, arista4]
#    print("in func")
#    print(my_dict)
    template_file = 'ex4_arista_config.j2'
    template = env.get_template(template_file)

#    config_list = []
#    for k, arista_device in my_list[0].items():
#        config = ""
#        config = template.render(**arista_device)
#        config_list.append(config)
    config = template.render(**my_dict)#arista_device)
#    config_list.append(config)
#    pprint(config_list)
#    print(config)
    return(config)
