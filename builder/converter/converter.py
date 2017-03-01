import yaml
import six
from builder.converter.converter_mapping import converters
import xml.etree.ElementTree as ET


# for reuse and avoid refactoring all current test functions,
# 2 types of results:
#   - only one item in ret, return as a tuple, not list
#   - multiple items in ret, return a tuple list
def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    ret = []
    for item in yaml_dict:
        yaml_view = item['view']
        view_name = yaml_view['name']
        xml = convert_yaml_dict_to_xml(yaml_view)
        xml_str = six.b("<?xml version=\"1.0\" ?>\n") + ET.tostring(xml, encoding="us-ascii")
        ret.append((view_name, xml_str))
    return ret[0] if (len(ret) == 1) else ret


def convert_yaml_dict_to_xml(yaml_dict):
    try:
        view_type = yaml_dict['type']
    except:
        raise Exception('View type %s not supported' % view_type)
    return converters[view_type](yaml_dict)
