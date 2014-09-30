import os
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.converter import convert_to_xml


class TestPipelineView(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "fixtures")

    def test_should_have_name_tag_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        name = xml_root.find('name')

        self.assertEqual(name.text, 'monsanto')

    def test_should_have_title_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        name = xml_root.find('buildViewTitle')

        self.assertEqual(name.text, 'build pipeline')

    def test_should_have_first_job_of_the_pipeline(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        first_job = xml_root.find('gridBuilder/firstJob')

        self.assertEqual(first_job.text, 'joby job')

    def test_should_include_number_of_displayed_builds(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        displayed_builds = xml_root.find('noOfDisplayedBuilds')

        self.assertEqual(displayed_builds.text, '20')

    def test_should_set_refresh_frequency(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        refresh_frequency = xml_root.find('refreshFrequency')

        self.assertEqual(refresh_frequency.text, '5')

    def test_should_trigger_only_latest(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        trigger_latest = xml_root.find('triggerOnlyLatestJob')

        self.assertEqual(trigger_latest.text, 'true')

    def test_should_set_pipeline_parameters(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        show_pipeline_params = xml_root.find('showPipelineParameters')
        show_pipeline_params_headers = xml_root.find('showPipelineParametersInHeaders')
        starts_with_params = xml_root.find('startsWithParameters')
        show_pipeline_defn_header = xml_root.find('showPipelineDefinitionHeader')

        self.assertEqual(show_pipeline_params.text, 'false')
        self.assertEqual(show_pipeline_params_headers.text, 'false')
        self.assertEqual(starts_with_params.text, 'false')
        self.assertEqual(show_pipeline_defn_header.text, 'false')

    def test_should_set_allow_manual_trigger(self):
        yaml_file = open(os.path.join(self.file_path, 'pipeline_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)

        always_allow_manual_trigger = xml_root.find('alwaysAllowManualTrigger')

        self.assertEqual(always_allow_manual_trigger.text, 'true')
