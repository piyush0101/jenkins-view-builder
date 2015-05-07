import os
from unittest import TestCase
from builder.converter.converter import convert_to_xml


class TestConverter(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "fixtures")

    def test_should_raise_exception_for_invalid_view_type(self):
        yaml_file = open(os.path.join(self.file_path, 'invalid_view_type.yaml'), 'r')

        yaml = yaml_file.read()

        self.assertRaises(lambda: convert_to_xml(yaml))
