import os
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_dict):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates/pipeline_view_template.xml')
    root = ET.parse(template_path).getroot()

    set_name(root, yaml_dict)
    set_title(root, yaml_dict)
    set_first_job(root, yaml_dict)
    set_displayed_builds(root, yaml_dict)
    set_refresh_frequency(root, yaml_dict)
    set_pipeline_params(root, yaml_dict)

    return root


def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict['name']


def set_title(root, yaml_dict):
    title = root.find('buildViewTitle')
    title.text = yaml_dict.get('title', yaml_dict['name'])


def set_first_job(root, yaml_dict):
    if 'first_job' not in yaml_dict:
        raise Exception("Missing 'first_job' parameter for pipeline view.")

    first_job = root.find('gridBuilder/firstJob')
    first_job.text = yaml_dict['first_job']


def set_displayed_builds(root, yaml_dict):
    displayed_builds = root.find('noOfDisplayedBuilds')
    displayed_builds.text = str(yaml_dict.get('no_of_displayed_builds', 1))


def set_refresh_frequency(root, yaml_dict):
    refresh_frequency = root.find('refreshFrequency')
    refresh_frequency.text = str(yaml_dict.get('refresh_frequency', 3))


def set_pipeline_params(root, yaml_dict):
    trigger_only_latest = root.find('triggerOnlyLatestJob')
    allow_manual_trigger = root.find('alwaysAllowManualTrigger')
    show_pipeline_params = root.find('showPipelineParameters')
    show_pipeline_params_headers = root.find('showPipelineParametersInHeaders')
    show_pipeline_defn_header = root.find('showPipelineDefinitionHeader')
    starts_with_params = root.find('startsWithParameters')

    trigger_only_latest.text = str(bool(yaml_dict.get('trigger_only_latest', False))).lower()
    allow_manual_trigger.text = str(bool(yaml_dict.get('always_allow_manual_trigger', False))).lower()
    show_pipeline_params.text = str(bool(yaml_dict.get('show_pipeline_parameters', False))).lower()
    show_pipeline_params_headers.text = str(bool(yaml_dict.get('show_pipeline_parameters_in_headers', False))).lower()
    show_pipeline_defn_header.text = str(bool(yaml_dict.get('show_pipeline_definition_header', False))).lower()
    starts_with_params.text = str(bool(yaml_dict.get('starts_with_parameters', True))).lower()
