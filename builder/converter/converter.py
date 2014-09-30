import yaml
from converter_mapping import converters

def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    try:
        view_type = yaml_dict[0]['view']['type']
    except:
        raise Exception('View type %s not supported' % view_type)
    return converters[view_type](yaml_str)
