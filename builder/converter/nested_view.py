import yaml
import os
import xml.etree.ElementTree as ET

def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(
        current_dir, 'templates/nested_view_template.xml')
    root = ET.parse(template_path).getroot()
    set_name(root, yaml_dict)
    xml = ET.tostring(root, method='xml', encoding="us-ascii")
    return (yaml_dict[0]['view']['name'],
            "<?xml version=\"1.0\" ?>" + xml)

def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict[0]['view']['name']