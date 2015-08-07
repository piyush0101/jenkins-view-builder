import os
from column_mapping import mapping
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_dict):
    root = get_xml_from_template('sectioned_view_template.xml')
    set_name(root, yaml_dict)
    set_sections(root, yaml_dict)
    return root


def get_xml_from_template(template_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates', template_name)

    return ET.parse(template_path).getroot()


def set_sections(root, yaml_dict):
    sections = root.find('sections')
    dict_sections = yaml_dict.get('sections')
    if dict_sections:
        for yaml_section in dict_sections:
            section = convert_section_yaml_dict_to_xml(yaml_section['section'])
            sections.append(section)


def convert_section_yaml_dict_to_xml(yaml_dict):
    type = yaml_dict['type']
    if type == 'text':
        return convert_text_section_to_xml(yaml_dict)
    elif type == 'list-view':
        return convert_list_view_section_to_xml(yaml_dict)
    elif type == 'view-listing':
        return convert_view_listing_section_to_xml(yaml_dict)
    else:
        raise Exception("Invalid section 'type' in yaml definition: %s" % type)


def convert_text_section_to_xml(yaml_dict):
    section_xml = get_xml_from_template('sectioned_view_text_section_template.xml')
    set_name(section_xml, yaml_dict)
    section_xml.find('text').text = yaml_dict['text']
    return section_xml


def convert_list_view_section_to_xml(yaml_dict):
    section_xml = get_xml_from_template('sectioned_view_list_view_section_template.xml')
    set_name(section_xml, yaml_dict)
    set_regex(section_xml, yaml_dict)
    set_jobs(section_xml, yaml_dict)
    set_columns(section_xml, yaml_dict)
    set_job_filters(section_xml, yaml_dict)
    return section_xml


def convert_view_listing_section_to_xml(yaml_dict):
    section_xml = get_xml_from_template('sectioned_view_view_listing_section_template.xml')
    set_name(section_xml, yaml_dict)
    set_columns_count(section_xml, yaml_dict)
    set_views(section_xml, yaml_dict)
    return section_xml


def set_name(root, yaml_dict):
    root.find('name').text = yaml_dict['name']


def set_regex(root, yaml_dict):
    if 'regex' in yaml_dict:
        element = ET.Element('includeRegex')
        element.text = yaml_dict['regex']
        root.append(element)


def set_jobs(root, yaml_dict):
    if 'jobs' in yaml_dict:
        jobs_section = root.find('jobNames')
        jobs = sorted(yaml_dict['jobs'], key=lambda s: s.lower())
        job_elements = [create_string_element(job) for job in jobs]
        for element in job_elements:
            jobs_section.append(element)


def set_views(root, yaml_dict):
    if 'views' in yaml_dict:
        views_section = root.find('views')
        views = yaml_dict['views']
        view_elements = [create_string_element(view) for view in views]
        for element in view_elements:
            views_section.append(element)


def set_columns(root, yaml_dict):
    columns = []
    if 'columns' not in yaml_dict:
        columns = [
            'status',
            'weather',
            'job',
            'last_success',
            'last_failure',
            'last_duration',
            'build_button'
        ]
    else:
        columns = yaml_dict['columns']

    columns_section = root.find('columns')
    column_elements = [create_column_element(column) for column in columns]
    for element in column_elements:
        columns_section.append(element)


def set_columns_count(root, yaml_dict):
    root.find('columns').text = str(yaml_dict['columns'])


def set_job_filters(root, yaml_dict):
    job_filters = root.find('jobFilters')
    dict_filters = yaml_dict.get('job-filters')
    if dict_filters:
        for yaml_section in dict_filters:
            job_filter = convert_job_filter_yaml_dict_to_xml(yaml_section['job-filter'])
            job_filters.append(job_filter)


def convert_job_filter_yaml_dict_to_xml(yaml_dict):
    type = yaml_dict['type']
    if type == 'job-status':
        return convert_job_status_filter_to_xml(yaml_dict)
    elif type == 'job-regex':
        return convert_job_regex_filter_to_xml(yaml_dict)
    elif type == 'other-views':
        return convert_other_views_filter_to_xml(yaml_dict)
    else:
        raise Exception("Invalid job-filter 'type' in yaml definition: %s" % type)


def convert_job_status_filter_to_xml(yaml_dict):
    filter_xml = get_xml_from_template('sectioned_view_job_status_filter_template.xml')
    for status in ['unstable', 'failed', 'aborted', 'disabled', 'stable']:
        set_job_status(filter_xml, yaml_dict, status)
    set_include_exclude_string(filter_xml, yaml_dict)
    return filter_xml


def convert_job_regex_filter_to_xml(yaml_dict):
    filter_xml = get_xml_from_template('sectioned_view_job_regex_filter_template.xml')
    set_include_exclude_string(filter_xml, yaml_dict)
    if 'regex' in yaml_dict:
        filter_xml.find('regex').text = yaml_dict['regex']
    if 'value-type' in yaml_dict:
        value_type = yaml_dict['value-type']
        if value_type not in ['NAME', 'DESCRIPTION', 'SCM', 'EMAIL', 'MAVEN', 'SCHEDULE', 'NODE']:
            raise Exception("Invalid 'value-type' in yaml definition.")
        filter_xml.find('valueTypeString').text = value_type
    return filter_xml

def convert_other_views_filter_to_xml(yaml_dict):
    filter_xml = get_xml_from_template('sectioned_view_other_views_filter_template.xml')
    set_include_exclude_string(filter_xml, yaml_dict)
    if 'other-view' in yaml_dict:
        filter_xml.find('otherViewName').text = yaml_dict['other-view']
    return filter_xml


def set_job_status(root, yaml_dict, status):
    if status in yaml_dict:
        root.find(status).text = str(yaml_dict[status]).lower()


def set_include_exclude_string(root, yaml_dict):
    type = yaml_dict['include-exclude-type']
    if type not in ['includeMatched', 'includeUnmatched', 'excludeMatched', 'excludeUnmatched']:
        raise Exception("Missing 'include-exclude-type' in yaml definition.")
    root.find('includeExcludeTypeString').text = type


def create_column_element(column):
    column_name = mapping.get(column, None)
    if column_name:
        column_element = ET.Element(column_name)
    else:
        raise Exception('Bad column name - %s' % column)
    return column_element


def create_string_element(name):
    job_element = ET.Element('string')
    job_element.text = name
    return job_element
