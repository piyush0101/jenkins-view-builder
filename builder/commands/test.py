import os
import shutil
import logging
import argparse

from cliff.command import Command
from builder.converter.converter import convert_to_xml


class Test(Command):
    """
    Spits out the generated xmls for input yaml(s) in the configurable out folder
    """
    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = argparse.ArgumentParser(description="Parser")
        parser.add_argument("yaml",
                            type=str,
                            nargs="+",
                            help="Path to the view yaml file")
        parser.add_argument("-o",
                            "--out-dir",
                            type=str,
                            dest="out_dir",
                            default="out",
                            help="Path to XML output dir")
        return parser

    def take_action(self, parsed_args):
        out_dir = parsed_args.out_dir
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir, ignore_errors=True)
        os.makedirs(out_dir)
        for yaml_filename in parsed_args.yaml:
            self.log.debug("Testing view file %s" % yaml_filename)
            with open(os.path.join(yaml_filename), 'r') as yaml_file:
                yaml = yaml_file.read()
                self.log.debug(yaml)

            try:
                name, xml = convert_to_xml(yaml)
            except Exception as e:
                raise(e)

            with open(os.path.join(out_dir, name + ".xml"), 'w') as xml_file:
                xml_file.write(xml)
