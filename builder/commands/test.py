import os
import shutil
import ConfigParser
import logging
import sys
import argparse

from cliff.command import Command
from builder.converter.converter import convert_to_xml
from builder.uploader.jenkins_upload import update


class Test(Command):
    "Spits out the generated xmls in the out folder of cwd"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = argparse.ArgumentParser(description="Parser")
        parser.add_argument("yaml",
                            type=str,
                            help="Path to the view yaml file")
        return parser

    def take_action(self, parsed_args):
        with open(os.path.join(parsed_args.yaml), 'r') as yaml_file:
            yaml = yaml_file.read()
            self.log.debug(yaml)

        try:
            name, xml = convert_to_xml(yaml)
        except Exception as e:
            raise(e)
        if os.path.isdir("out"):
            shutil.rmtree("out", ignore_errors=True)
        os.makedirs("out")
        with open(os.path.join("out", name + ".xml"), 'w') as xml_file:
            xml_file.write(xml)
