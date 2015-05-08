#!/usr/bin/env/python

PROJECT = 'jenkins-view-builder'

VERSION = '0.5.0'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'name': 'jenkins-view-builder',
    'version': '0.5.0',

    'description': 'Build jenkins views in YAML',

    'author': 'Piyush Srivastava',
    'author_email': 'piyush.0101@gmail.com',

    'url': 'https://github.com/piyush0101/jenkins-view-builder',
    'download_url': 'https://github.com/piyush0101/jenkins-view-builder/archive/0.5.0.tar.gz',

    'classifiers': [],

    'platforms': ['Any'],

    'scripts': [],

    'provides': [],

    'install_requires': [
        'cliff',
        'PyYAML',
        'argparse',
        'cmd2',
        'prettytable',
        'pyparsing',
        'six',
        'stevedore',
        'wsgiref',
        'requests'
    ],

    'packages': find_packages(),
    'include_package_data': True,
    'package_data': {'builder.converter.template': ['*.xml']},

    'entry_points': {
        'console_scripts': [
            'jenkins-view-builder = builder.main:main',
        ],
        'builder.commands': [
            'simple = builder.commands.simple:Simple',
            'update = builder.commands.update:Update',
            'test = builder.commands.test:Test',
        ],
    },


    'zip_safe': False,
}

setup(**config)
