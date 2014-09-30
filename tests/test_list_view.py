import os
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.converter import convert_to_xml
from builder.converter.list_view import create_job_element
from builder.converter.list_view import create_column_element


class TestListView(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "fixtures")

    def test_should_have_a_name_tag_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'list_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)
        name = xml_root.find('name')

        self.assertEqual(name.text, 'monsanto')

    def test_should_have_jobs_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'list_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)
        jobs = xml_root.findall('jobNames/string')
        jobs = [job.text for job in jobs]

        self.assertListEqual(jobs, ['Merge-nova-Ply',
                                    'Merge-config-Ply',
                                    'Merge-bark-Ply'])

    def test_should_have_columns_in_view_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'list_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)
        columns = xml_root.findall('columns/')
        column_tags = [column.tag for column in columns]

        self.assertListEqual(column_tags, ['hudson.views.StatusColumn',
                                           'hudson.views.WeatherColumn'])

    def test_should_include_recurse_flag_in_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'list_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)
        recurse = xml_root.find('recurse')

        self.assertEqual(recurse.text, 'false')

    def test_should_include_description_in_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'list_view.yaml'), 'r')

        yaml = yaml_file.read()

        name, xml_view = convert_to_xml(yaml)
        xml_root = ET.fromstring(xml_view)
        description = xml_root.find('description')

        self.assertEqual(description.text, 'Merge ply jobs')

    def test_should_create_a_job_element_given_job_name(self):
        job_name = 'jobyjob'
        element = create_job_element(job_name)
        self.assertEqual(element.text, job_name)

    def test_should_create_a_column_element_given_name(self):
        column_name = 'status'
        expected_name = 'hudson.views.StatusColumn'
        element = create_column_element(column_name)
        self.assertEqual(element.tag, expected_name)

    def test_should_raise_an_exception_given_a_bad_column_name(self):
        column_name = 'other'
        self.assertRaises(Exception,
                          lambda: create_column_element(column_name))
