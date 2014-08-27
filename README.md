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

jenkins-view-builder as of now only supports **List View** with support for other views coming soon. Views are specified as yaml files and given to the jenkins-view-builder to upload to jenkins. Say, you have the following **List View** view in a yaml file

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

jenkins-view-builder can create this view in jenkins. jenkins-view-builder needs a jenkins config file which tells it how to connect to jenkins. The config file looks like this

        [jenkins]
        user=user
        password=password
        url=http[s]://jenkinsurl
        
Once that is ready, we are all set to create the view in jenkins using the following command

        jenkins-view-builder update --conf path-to-jenkins-config-file path-to-view-yaml-file
        
There should be feedback on stdout on what the tool is doing. update command is capable of determining if the view already exists and if it does then it just updates it. 

It is also possible to test the view to make sure that jenkins-view-builder is creating the correct xml that it would post to jenkins. This can be done using the following command

        jenkins-view-builder test path-to-view-yaml-file

Running this command will spit out the generated xml in the `out` folder of the current working directory. If the output looks good, the previous `update` command can be used to upload the view.
