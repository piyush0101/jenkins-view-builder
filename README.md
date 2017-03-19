[![Build Status](https://snap-ci.com/piyush0101/jenkins-view-builder/branch/master/build_image)](https://snap-ci.com/piyush0101/jenkins-view-builder/branch/master)

jenkins-view-builder
====================

jenkins-view-builder is a command line tool for managing jenkins views with yaml files and back
your views with SCM.

Installation
---

Install jenkins-view-builder at a system level or in an isolated virtualenv by running the
following command:

        pip install jenkins-view-builder

Usage
---

There are several types of views in jenkins:
* Build Pipeline View
* Nested View
* Dashboard
* List View
* Radiator

jenkins-view-builder as of now supports **List View**, **Build Pipeline View** and **Nested View**
with support for other views coming soon. Examples of yaml files are in the `tests/fixtures`
folder. Views are specified as yaml files and given to the jenkins-view-builder to upload to
jenkins. Say, you have the following **List View** view in a yaml file

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
		- view:
			type: list
			name: second
			description: Second ply jobs
			columns:
				- status
			recurse: False

jenkins-view-builder can create this view in jenkins. jenkins-view-builder needs a jenkins config
file which tells it how to connect to jenkins. The config file looks like this

        [jenkins]
        user=user
        password=password
        url=http[s]://jenkinsurl
        
Once that is ready, we are all set to create the view in jenkins using the following command

        jenkins-view-builder update --conf path-to-jenkins-config-file path-to-view-yaml-file
        
There should be feedback on stdout on what the tool is doing. update command is capable of
determining if the view already exists and if it does then it just updates it. 

It is also possible to test the view to make sure that jenkins-view-builder is creating the correct
xml that it would post to jenkins. This can be done using the following command

        jenkins-view-builder test path-to-view-yaml-file

Running this command will spit out the generated xml in the `out` folder of the current working
directory. If the output looks good, the `update` command can be used to upload the view.

