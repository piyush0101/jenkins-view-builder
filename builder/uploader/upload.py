import requests
import ConfigParser
import argparse
import os
import sys
import re

views_dir = os.path.join(os.getcwd() + "/views")
views = [view for view in os.listdir(views_dir)]

headers = {'Content-type': 'text/xml'}


def parse_config(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    user = config.get('jenkins', 'user')
    password = config.get('jenkins', 'password')
    url = config.get('jenkins', 'url') + '/createView?name=%s'
    return dict(url=url, user=user, password=password)


def create_views(config):
    for view in views:
        with open(os.path.join(views_dir, view), 'r') as view_xml:
            view_name = re.search('(.*).(xml)', view).group(1)
            print "Creating view %s" % view_name
            payload = view_xml.read()
            response = requests.post(config['url'] % view_name,
                                     data=payload,
                                     headers=headers,
                                     auth=(config['user'],
                                           config['password']))
            if response.status_code != 200:
                print response.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creating Jenkins views")
    parser.add_argument("--conf",
                        type=str,
                        help="Path to the jenkins config file")
    args = parser.parse_args()
    if not args.conf:
        print parser.print_help()
        sys.exit(1)
    config = parse_config(args.conf)
    create_views(config)
