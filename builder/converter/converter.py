import yaml
from converter_mapping import converters
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    yaml_view = yaml_dict[0]['view']
    view_name = yaml_view['name']

    xml = convert_yaml_dict_to_xml(yaml_view)
    xml_str = ET.tostring(xml, method='xml', encoding="us-ascii")
    return (view_name, "<?xml version=\"1.0\" ?>" + xml_str)


def convert_yaml_dict_to_xml(yaml_dict):
    try:
        view_type = yaml_dict['type']
    except:
        raise Exception('View type %s not supported' % view_type)
    return converters[view_type](yaml_dict)
