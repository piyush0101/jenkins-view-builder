import yaml
import os
import xml.etree.ElementTree as ET
from column_mapping import mapping


def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir,
                                 'templates/list_view_template.xml')
    root = ET.parse(template_path).getroot()
    set_name(root, yaml_dict)
    set_description(root, yaml_dict)
    set_jobs(root, yaml_dict)
    set_columns(root, yaml_dict)
    set_recurse(root, yaml_dict)
    xml = ET.tostring(root, method='xml', encoding="us-ascii")
    return (yaml_dict[0]['view']['name'],
            "<?xml version=\"1.0\" ?>" + xml)


def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict[0]['view']['name']


def set_description(root, yaml_dict):
    if yaml_dict[0]['view']['description']:
        element = ET.Element('description')
        element.text = yaml_dict[0]['view']['description']
        root.append(element)


def set_jobs(root, yaml_dict):
    jobs_section = root.find('jobNames')
    jobs = yaml_dict[0]['view']['jobs']
    job_elements = [create_job_element(job)
                    for job in jobs]
    for element in job_elements:
        jobs_section.append(element)


def set_columns(root, yaml_dict):
    columns_section = root.find('columns')
    columns = yaml_dict[0]['view']['columns']
    column_elements = [create_column_element(column)
                       for column in columns]
    for element in column_elements:
        columns_section.append(element)


def set_recurse(root, yaml_dict):
    recurse = root.find('recurse')
    recurse.text = 'true' if yaml_dict[0]['view']['recurse'] else 'false'


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
