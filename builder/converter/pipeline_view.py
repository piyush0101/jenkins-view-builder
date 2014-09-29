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
