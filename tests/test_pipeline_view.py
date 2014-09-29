import os
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.pipeline_view import convert_to_xml


class TestPipelineView(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir + "/%s")

    def test_should_have_name_tag_in_view_xml(self):
        yaml_file = open(self.file_path % 'pipeline_view.yaml', 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        name = xml_root.find('name')

        self.assertEqual(name.text, 'monsanto')

    def test_should_have_title_in_view_xml(self):
        yaml_file = open(self.file_path % 'pipeline_view.yaml', 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        name = xml_root.find('buildViewTitle')

        self.assertEqual(name.text, 'build pipeline')

    def test_should_have_first_job_of_the_pipeline(self):
        yaml_file = open(self.file_path % 'pipeline_view.yaml', 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        first_job = xml_root.find('gridBuilder/firstJob')

        self.assertEqual(first_job.text, 'joby job')

    def test_should_include_number_of_displayed_builds(self):
        yaml_file = open(self.file_path % 'pipeline_view.yaml', 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        displayed_builds = xml_root.find('noOfDisplayedBuilds')

        self.assertEqual(displayed_builds.text, '20')
