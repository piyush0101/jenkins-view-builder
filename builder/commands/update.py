import os
import ConfigParser
import logging
import sys
import argparse

from cliff.command import Command
from builder.converter.list_view import convert_to_xml
from builder.uploader.jenkins_upload import update


class Update(Command):
    "Command for updating views on jenkins"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = argparse.ArgumentParser(description="Parser")
        parser.add_argument("--conf",
                            type=str,
                            help="Path to the jenkins config file")
        parser.add_argument("yaml",
                            type=str,
                            help="Path to the view yaml file")
        return parser


    def take_action(self, parsed_args):
        self.log.info("Updating view data in Jenkins")
        if not parsed_args.conf:
            print parser.print_help()
            sys.exit(1)
        config = self.parse_config(parsed_args.conf)
        with open(os.path.join(parsed_args.yaml), 'r') as yaml_file:
            yaml = yaml_file.read()
            self.log.debug(yaml)

        name, xml = convert_to_xml(yaml)
        update(config, name, xml)
    

    def parse_config(self, config_file):
        self.log.info("Parsing the jenkins config file")
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        user = config.get('jenkins', 'user')
        password = config.get('jenkins', 'password')
        url = config.get('jenkins', 'url') + '/createView?name=%s'
        return dict(url=url, user=user, password=password)
