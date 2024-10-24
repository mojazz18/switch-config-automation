import yaml
from jinja2 import Environment, FileSystemLoader
from inventory import INVENTORY
from rich import print as r_print
from netmiko import ConnectHandler

def generate_config(hostname):

    file_data_yaml = yaml.safe_load(open(f"hosts_vars/{hostname}.yaml"))
    #r_print(file_data_yaml)
    env_obj = Environment(loader=FileSystemLoader("./jinja_templates"), trim_blocks=True, lstrip_blocks=True)
    template_var = env_obj.get_template("cisco_config_template.j2")
    config = template_var.render(file_data_yaml)
    r_print(config)
    return config

#def send_config():

def main():

    for each_device in INVENTORY:
        generate_config(each_device["hostname"])




main()