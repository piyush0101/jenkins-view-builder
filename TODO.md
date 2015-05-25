TODO
====

Functional Tests
---

Functional Tests to test view creation in Jenkins. As of now there are tests which test translation of yaml files to xml files. There are no end to end tests that can actually go in jenkins, create views with jenkins-view-builder and assert that the creation of views was successful. Jenkins war comes with an embedded jetty server so it should be pretty straight forward to launch a virtual machine, run jenkins with a command like `java -jar jenkins.war`, create a couple of jobs and create different kinds of views programmatically and make sure those are created fine.
