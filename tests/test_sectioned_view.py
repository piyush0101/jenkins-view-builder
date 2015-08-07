import os
from unittest import TestCase
import xml.etree.ElementTree as ET
from builder.converter.converter import convert_to_xml


LIST_VIEW_SECTION_LOCATOR = 'sections/hudson.plugins.sectioned__view.ListViewSection'
TEXT_SECTION_LOCATOR = 'sections/hudson.plugins.sectioned__view.TextSection'
VIEW_LISTING_LOCATOR = 'sections/hudson.plugins.sectioned__view.ViewListingSection'

JOB_STATUS_FILTER_LOCATOR = 'hudson.views.JobStatusFilter'
JOB_REGEX_FILTER_LOCATOR = 'hudson.views.RegExJobFilter'
OTHER_VIEWS_FILTER_LOCATOR = 'hudson.views.OtherViewsFilter'


class TestSectionedView(TestCase):

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "fixtures")

    def load_test_xml(self):
        yaml_file = open(os.path.join(self.file_path, 'sectioned_view.yaml'), 'r')

        yaml = yaml_file.read()

        _, xml_view = convert_to_xml(yaml)
        return ET.fromstring(xml_view)

    def test_should_have_name_in_view_xml(self):
        xml_root = self.load_test_xml()

        name = xml_root.find('name')
        self.assertEqual(name.text, 'monsanto')

    def test_should_have_name_in_text_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(TEXT_SECTION_LOCATOR)
        self.assertEqual(section.find('name').text, 'text section name')

    def test_should_have_name_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        self.assertEqual(section.find('name').text, 'list-view section name')

    def test_should_have_regex_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        self.assertEqual(section.find('includeRegex').text, 'test-.*')

    def test_should_have_jobs_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        jobs = section.findall('jobNames/string')
        jobs = [job.text for job in jobs]
        self.assertListEqual(jobs, ['job1-test', 'job2-test', 'Job3-test'])

    def test_should_have_columns_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        columns = section.findall('columns/')
        column_tags = [column.tag for column in columns]
        self.assertListEqual(column_tags, ['hudson.views.StatusColumn',
                                           'hudson.views.WeatherColumn',
                                           'hudson.views.JobColumn'])

    def test_should_have_text_in_text_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(TEXT_SECTION_LOCATOR)
        self.assertEqual(section.find('text').text, 'text in text section')

    def test_should_have_views_in_view_listing_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(VIEW_LISTING_LOCATOR)
        views = section.findall('views/string')
        views = [view.text for view in views]
        self.assertListEqual(views, ['view1', 'view2'])

    def test_should_have_columns_in_view_listing_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(VIEW_LISTING_LOCATOR)
        self.assertEqual(section.find('columns').text, '3')

    def test_should_have_job_status_filter_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        filter = section.find('jobFilters/%s' % JOB_STATUS_FILTER_LOCATOR)
        self.assertEqual(filter.find('unstable').text, 'true')
        self.assertEqual(filter.find('stable').text, 'false')
        self.assertEqual(filter.find('failed').text, 'false')
        self.assertEqual(filter.find('disabled').text, 'false')
        self.assertEqual(filter.find('aborted').text, 'false')
        self.assertEqual(filter.find('includeExcludeTypeString').text, 'includeUnmatched')

    def test_should_have_job_regex_filter_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        filter = section.find('jobFilters/%s' % JOB_REGEX_FILTER_LOCATOR)
        self.assertEqual(filter.find('regex').text, 'test-node-.*')
        self.assertEqual(filter.find('valueTypeString').text, 'NODE')
        self.assertEqual(filter.find('includeExcludeTypeString').text, 'excludeMatched')

    def test_should_have_other_views_filter_in_list_view_section_xml(self):
        xml_root = self.load_test_xml()

        section = xml_root.find(LIST_VIEW_SECTION_LOCATOR)
        filter = section.find('jobFilters/%s' % OTHER_VIEWS_FILTER_LOCATOR)
        self.assertEqual(filter.find('otherViewName').text, 'OTHER_VIEW_NAME')
        self.assertEqual(filter.find('includeExcludeTypeString').text, 'excludeMatched')
