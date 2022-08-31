from jinja2 import Environment, FileSystemLoader

pers = [
    {'name': 'nick', 'age': 23},
    {'name': 'nick2', 'age': 232},
    {'name': 'nic3', 'age': 233},
]

env = Environment(loader=FileSystemLoader(''))

templ = env.get_template('main.htm')

print(templ.render(users = pers))
