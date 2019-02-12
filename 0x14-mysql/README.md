# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---  

I wrote a blog explaining these concepts: What is a primary-replica cluster, MySQL primary replica setup, and Build a robust database backup strategy.  
Then I deleted it after it was graded.


## Each scripts and their output?**  
* Script 0 and Script 1- Install and configure MySQL on web-01 and web-02 so that they form a primary/replica (master/slave) cluster.

Having a replica member on for your MySQL database has 2 advantages:

Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed.  

MySQL primary must be hosted on web-01 - do not use the bind-address, just comment this parameter
MySQL replica must be hosted on web-02
Setup replication for the MySQL database named holberton
Provide your MySQL primary configuration as answer file(my.cnf) with the name 0-mysql_configuration_primary
Provide your MySQL replica configuration as an answer file with the name 0-mysql_configuration_replica  

What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.  

Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.  



#### Limitations of these projects:  
___

-Allowed editors: vi, vim, emacs  
-All your files will be interpreted on Ubuntu 14.04 LTS  
-All your files should end with a new line  
-A README.md file, at the root of the folder of the project, is mandatory  
-All your Bash script files must be executable  
-You are not allowed to use awk  
-Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error  
-The first line of all your Bash scripts should be exactly #!/usr/bin/env bash  
-The second line of all your Bash scripts should be a comment explaining what is the script doing  

