import os
import xml.etree.ElementTree as ET


def write_to_disk(xml, path):
    view_xml = ET.fromstring(xml)
    view_name = view_xml.find('name').text
    with open(os.path.join(path, view_name + ".xml"), 'w') as view_file:
        view_file.write(xml)
