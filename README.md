# cloud-deployment-2
Deploy a cluster of (virtual) computers on CloudLab 

Assignment 2 (15 points)¶
Part 1: Modify the default experiment profile from class lecture (5 points):
This part of the assignment will use the repository that you forked in the CloudLab geni-lab lecture:

Modify the profile.py such that:
It uses the CENTOS7-64-STD image and has a public IP interface
It uses a XenVM instead of a RawPC compute hardware
Modify the silly.sh file so that it contains the command to update the package and installs apache2
Make sure that all changes are committed
Instantiate the profile and confirm that the experiment is working as intended (one should be able to access the public IP address at port 80 and view the default Apache web page (Testing 1 2 3).
Part 2: Deploy a cluster of (virtual) computers on CloudLab (10 points):
Create a 4-node cluster on CloudLab with the following requirements:

The Github repository for this assignment should be named cloud-deployment-2 (2 points)
The cluster should have 4 compute nodes, deployed as XenVM and run CentOS7-64-STD distro (2 points)
The 4 compute nodes should be named node-1 through node-4, and have their local IP addresses range from 192.168.1.1 to 192.168.1.4 accordingly. (4 points)
The first compute node, named node-1, should also have a public ID address. (2 points)
Submission:
Each student should submit a text file (txt or pdf) to D2L containing the following:

The URL to the repository containing Part 1 on your Github account
The URL to the experiment instance of Part 1 on CloudLab (should be instantiated the moment you submit the assignment on D2L)
The URL to the repository containing Part 2 on your Github account
The URL to the experiment instance of Part 2 on CloudLab (should be instantiated the moment you submit the assignment on D2L)
You must also email me immediately once you submit the assignment on D2L. As there is a timer on CloudLab experiment, I will attempt to grade your assignment as soon as possible, and I will assume that I have between 12 to 16 hours (see Submission condition) to grade.

This is an individual assignment. Each student should have their own individual submission.
