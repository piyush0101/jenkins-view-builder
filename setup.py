
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Build jenkins views in YAML',
    'author': 'Piyush Srivastava',
    'url': 'http://jenkins-view-builder.com',
    'download_url': 'Where to download it.',
    'author_email': 'piyush.0101@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['jenkins-view-builder'],
    'scripts': [],
    'name': 'jenkins-view-builder'
}

setup(**config)
