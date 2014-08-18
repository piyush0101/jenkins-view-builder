import os
import unittest
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.views import write_to_disk


class TestViews(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir + "/%s")

    @unittest.skip('Unfinished')
    def test_should_write_to_disk(self):
        view_xml = open(self.file_path % 'list_view.xml')
        xml = view_xml.read()

        view_name = ET.fromstring(xml).find('name').text
        path = "views"
        write_to_disk(xml, path)

        written_file = open(os.path.join(path, 'monsanto.xml'), 'r')
        disk_xml = written_file.read()

        self.assertEqual(disk_xml, xml)
