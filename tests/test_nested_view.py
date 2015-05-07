import os
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.converter import convert_to_xml


class TestNestedView(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "fixtures")

    def test_should_have_name_tag_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'nested_view.yaml'), 'r')

        yaml = yaml_file.read()

        _, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        name = xml_root.find('name')

        self.assertEqual(name.text, 'monsanto')
