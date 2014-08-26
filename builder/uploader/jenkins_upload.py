import requests
import ConfigParser
import argparse
import os
import sys
import re

headers = {'Content-type': 'text/xml'}


def post(url, payload, config):
    response = requests.post(url,
                             data=payload,
                             headers=headers,
                             auth=(config['user'],
                                   config['password']),
                             verify=False)
    if response.status_code != 200:
        print response.text


def update(config, view_name, view_xml):
        get_url = config['url'] + '/view/%s' % view_name
        create_url = config['url'] + '/createView?name=%s' % view_name
        update_url = get_url + '/config.xml'
        response = requests.get(get_url, verify=False)
        if response.status_code != 200:
            print "Creating view %s" % view_name
            post(create_url, view_xml, config)
        else:
            print "Updating view %s" % view_name
            post(update_url, view_xml, config)
