import yaml
import os
import xml.etree.ElementTree as ET


def convert_to_xml(yaml_str):
    yaml_dict = yaml.load(yaml_str)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(
        current_dir, 'templates/pipeline_view_template.xml')
    root = ET.parse(template_path).getroot()
    set_name(root, yaml_dict)
    set_title(root, yaml_dict)
    set_first_job(root, yaml_dict)
    set_displayed_builds(root, yaml_dict)
    set_refresh_frequency(root, yaml_dict)
    set_trigger_only_latest(root, yaml_dict)
    set_pipeline_params(root, yaml_dict)
    set_allow_manual_trigger(root, yaml_dict)
    xml = ET.tostring(root, method='xml', encoding="us-ascii")
    return (yaml_dict[0]['view']['name'],
            "<?xml version=\"1.0\" ?>" + xml)


def set_name(root, yaml_dict):
    name = root.find('name')
    name.text = yaml_dict[0]['view']['name']


def set_title(root, yaml_dict):
    title = root.find('buildViewTitle')
    title.text = yaml_dict[0]['view']['title']


def set_first_job(root, yaml_dict):
    first_job = root.find('gridBuilder/firstJob')
    first_job.text = yaml_dict[0]['view']['first_job']


def set_displayed_builds(root, yaml_dict):
    displayed_builds = root.find('noOfDisplayedBuilds')
    displayed_builds.text = str(yaml_dict[0]['view']['no_of_displayed_builds'])


def set_refresh_frequency(root, yaml_dict):
    refresh_frequency = root.find('refreshFrequency')
    refresh_frequency.text = str(yaml_dict[0]['view']['refresh_frequency'])


def set_trigger_only_latest(root, yaml_dict):
    trigger_only_latest = root.find('triggerOnlyLatestJob')
    trigger_only_latest.text = 'true' if str(
        yaml_dict[0]['view']['trigger_only_latest']) else 'false'


def set_pipeline_params(root, yaml_dict):
    show_pipeline_params = root.find('showPipelineParameters')
    starts_with_params = root.find('startsWithParameters')
    show_pipeline_params_headers = root.find('showPipelineParametersInHeaders')
    show_pipeline_defn_header = root.find('showPipelineDefinitionHeader')

    view = yaml_dict[0]['view']

    show_pipeline_params.text = 'true'  if view['show_pipeline_parameters'] else 'false'
    starts_with_params.text = 'true' if view['starts_with_parameters'] else 'false'
    show_pipeline_params_headers.text = 'true' if view['show_pipeline_parameters_in_headers'] else 'false'
    show_pipeline_defn_header.text = 'true' if view['show_pipeline_definition_header'] else 'false'


def set_allow_manual_trigger(root, yaml_dict):
    allow_manual_trigger = root.find('alwaysAllowManualTrigger')
    allow_manual_trigger.text = 'true' if str(
        yaml_dict[0]['view']['always_allow_manual_trigger']) else 'false'
