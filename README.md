jenkins-view-builder
====================

jenkins-view-builder is a command line tool for managing jenkins views with yaml files and back your views with SCM. As of now the `jenkins-view-builder` is not available as a PyPi package so it would require some manual steps for installing.

Installation
---

Clone the `jenkins-view-builder` repository and install it in a virtualenv using the following steps

    git clone https://github.rackspace.com/O3Eng-infra/jenkins-view-builder
    virtualenv .venv
    source .venv/bin/activate
    python setup.py install

This should setup the `jenkins-view-builder`.

Usage
---

There are several types of views in jenkins
* Build Pipeline View
* Nested View
* Dashboard
* List View
* Radiator

jenkins-view-builder as of now only supports List View with support for other views coming soon. Views are specified as yaml files and given to the jenkins-view-builder to upload to jenkins. Say, you have the following `list` view in a yaml file

        - view:
          type: list
          name: monsanto
          description: Merge ply jobs
          jobs:
           - Merge-nova-Ply
           - Merge-config-Ply
           - Merge-bark-Ply    
          columns:
           - status
           - weather
          recurse: False

You can use the jenkins-view-builder to create this view in jenkins. Before doing that, you would need to have a jenkins config file which tells the jenkins-view-builder how to connect to jenkins. The config file looks like this

        [jenkins]
        user=user
        password=password
        url=http[s]://jenkinsurl
        
Once you have that ready, you are all set to create the view in jenkins using the following command

        jenkins-view-builder update --conf path-to-jenkins-config-file update path-to-view-yaml-file
        
You should see feedback from the logs on what the jenkins-view-builder is doing. 

        







