import os
import converter
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_dict):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates/nested_view_template.xml')

    root = ET.parse(template_path).getroot()
    set_name(root, yaml_dict)
    set_views(root, yaml_dict)
    set_default_view(root, yaml_dict)
    return root


def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict['name']


def set_views(root, yaml_dict):
    if 'views' not in yaml_dict:
        raise Exception("Missing 'views' section for nested view.")

    views_section = root.find('views')
    for yaml_view in yaml_dict['views']:
        view = converter.convert_yaml_dict_to_xml(yaml_view['view'])
        views_section.append(view)


def set_default_view(root, yaml_dict):
    if 'defaultView' in yaml_dict:
        defaultView = root.find('defaultView')
        defaultView.text = yaml_dict['defaultView']
