import os
from column_mapping import mapping
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_dict):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates/list_view_template.xml')
    root = ET.parse(template_path).getroot()

    set_name(root, yaml_dict)
    set_description(root, yaml_dict)
    set_jobs(root, yaml_dict)
    set_columns(root, yaml_dict)
    set_recurse(root, yaml_dict)
    set_regex(root, yaml_dict)

    return root


def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict['name']


def set_description(root, yaml_dict):
    if 'description' in yaml_dict:
        element = ET.Element('description')
        element.text = yaml_dict['description']
        root.append(element)


def set_jobs(root, yaml_dict):
    if 'jobs' in yaml_dict:
        jobs_section = root.find('jobNames')
        jobs = yaml_dict['jobs']
        job_elements = [create_job_element(job) for job in jobs]
        for element in job_elements:
            jobs_section.append(element)


def set_columns(root, yaml_dict):
    columns = []
    if 'columns' not in yaml_dict:
        columns = [
            'status',
            'weather',
            'job',
            'last_success',
            'last_failure',
            'last_duration',
            'build_button'
        ]
    else:
        columns = yaml_dict['columns']

    columns_section = root.find('columns')
    column_elements = [create_column_element(column) for column in columns]
    for element in column_elements:
        columns_section.append(element)


def set_recurse(root, yaml_dict):
    if 'recurse' not in yaml_dict:
        return
    recurse = root.find('recurse')
    recurse.text = 'true' if yaml_dict['recurse'] else 'false'


def set_regex(root, yaml_dict):
    if 'includeRegex' in yaml_dict:
        element = ET.Element('includeRegex')
        element.text = yaml_dict['includeRegex']
        root.append(element)


def create_column_element(column):
    column_name = mapping.get(column, None)
    if column_name:
        column_element = ET.Element(column_name)
    else:
        raise Exception('Bad column name - %s' % column)
    return column_element


def create_job_element(name):
    job_element = ET.Element('string')
    job_element.text = name
    return job_element
