import requests
import ConfigParser
import argparse
import os
import sys
import re

headers = {'Content-type': 'text/xml'}

def update(config, view_name, view_xml):
        print "Creating view %s" % view_name
        payload = view_xml
        response = requests.post(config['url'] % view_name,
                                 data=payload,
                                 headers=headers,
                                 auth=(config['user'], 
                                       config['password']))
        if response.status_code != 200:
            print response.text
