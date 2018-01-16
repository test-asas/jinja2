from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('intf_config.tpl')

vardata = {
    'if_name': 'GigabitEthernet1',
    'if_description': 'To_Router',
    'ipv4addr': '10.0.0.1',
    'netmask':  '255.255.255.0'
}

config = template.render(vardata)
print(config)