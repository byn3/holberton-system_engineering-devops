# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---  

**What is a PID?**  
*.*  

**What is a process?**  
*.*  

**How to find a process’ PID?**  
*.*  

**How to kill a process?**  
*.*  

**What is a signal?**  
*.*  

**What are the 2 signals that cannot be ignored?**  
*.* 

## Each scripts and their output?**  
* Script 0 - Write a Bash script that displays its own PID.      
* Script 1 - Write a Bash script that displays a list of currently running processes.    
* Script 2 - write a Bash script that displays line containing the bash word, thus allowing you to easily get the PID of your Bash process.      
* Script 3 - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.    
* Script 4 - Write a Bash script that displays To infinity and beyond indefinitely.    
* Script 5 - We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.      
* Script 6 - Write a Bash script that kills 4-to_infinity_and_beyond process.      
* Script 7 - Write a Bash script that displays:     
* Script 8 - Write a Bash script that kills the process 7-highlander.      


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





Readme
What is localhost
What is 0.0.0.0
What is the hosts file
Netcat examples
man or help: ifconfig, telnet, nc, cut

What you should learn from this project
At the end of this project you are expected to be able to explain, without the help of Google:











What is localhost/127.0.0.1
Localhost means this computer. It uses loopback method to bypass local network
hardware. localhost will normally resolve to the IPv4 loopback address of
127.0.0.1. In IPv6 loopback is at ::1.


What is 0.0.0.0
In IPv6, 0.0.0.0 is a non-routable metaaddress used to designate a invalid,
unknown, or nonapplicable target. This address has a special meaning depending
on a lot of stuff. 0.0.0.0 could mean any IPv4 address (INADDR\_ANY), it could
mean other things.
:: is IPv6's version of 0.0.0.0. 

What is /etc/hosts
The hosts file is a text file that all OS uses to translate hostnames into ip
addresses. Eg. typing in google.com or facebook.com the system will look into
the host file and find the IP address of the appropriate server. But not all
sites are on the file. The computer will first look into the host file and if
the site is not there then it will go to the DNS server in the network's
setting (usually the ISPs DNS servers).
But you can use the host file to add the servers that the DNS cannot provide.
Like some dark net shit. Or aliases for the local network.

How to display your machine’s active network interfaces
Netcat or nc. Useful to debug or monitor network stuff. We can create UDP or
TCP connections and also analyze them. We can write scripts that handle TCP and
UDP sockets. Here are some nc stuff
https://www.thegeekstuff.com/2012/04/nc-command-examples/

