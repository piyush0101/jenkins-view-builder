import logging
import sys
import argparse

from cliff.command import Command


class Update(Command):
    "Command for updating views on jenkins"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = argparse.ArgumentParser(description="Parser")
        parser.add_argument("--conf",
                            type=str,
                            help="Path to the jenkins config file")
        return parser

    def take_action(self, parsed_args):
        self.log.info("Updating view data in Jenkins")
        if not parsed_args.conf:
            print parser.print_help()
            sys.exit(1)

        print parsed_args.conf

        # convert given yaml to xml
        # if given a directory, get all the yamls from in there and convert
        # upload xml to jenkins
        # do not create if the view already exists
        # in that case update instead

