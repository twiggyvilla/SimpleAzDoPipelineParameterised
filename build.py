from jinja2 import Template
import sys
import os

appname = sys.argv[1]

template_directory = "templates"

def process_templates(template_directory, vars):
    for filename in os.listdir(template_directory):
        print(filename)
        template_file_object = open(template_directory + '/' + filename)
        jinja_template = Template(template_file_object.read())
        rendered_template = jinja_template.render(vars)
        print(rendered_template)

vars = {}
vars['appname'] = appname

process_templates(template_directory, vars)
