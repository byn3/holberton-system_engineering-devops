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




What DNS stands for
What is DNS main role
What are DNS record types for:
	•	A
	•	CNAME
	•	TXT
	•	MX
What is the main role of a web server
What is a child process
Why web server usually have a parent process and child processes
What are the main HTTP requests




Lean/agile method focuses on iterating as fast as possible. Code, ship, measure impact, learn, fix or improve, start over. 
A big advantage of this is if product development is good, fast iterations allow quick detections and avoids wasting time. Quicker iterations means fewer lines of code being pushed at every deploy so performance impact measurement is easy and so is troubleshooting. 
CI/CD is continuous integration and continuous deployment. Allows lean/agile way of working.
This is a shipping pipeline. 
Ship the code with Capistrano or Fabric.
Encapsulate code with Docker or Packer.
Test the code with Jenkins, CircleCi, or Travis.
Measure the code with Datadog, Newrelic, or Wavefront.

Code, build, test, release, deploy, operate, monitor, plan, code.
https://blog.versionone.com/understanding-ci-in-cd/

Lean is eliminating or reducing the non-value added activities (wastes) and increases value. Agile is part of the lean and also tries to achieve customer alignment and quality and speed.

"Eliminating waste means eliminating useless meetings, tasks and documentation"
Highest priorities of Agile is customer satisfaction, changing requirements, frequent delivery, developers and business coexisting, simplicity, etc. Very specific agile is scrum or kanban. 

TURDUCKEN : Lean, Agile, Scrum.


Containers are better than VM because it reduces OS glut. Containers make CI/CD faster. Most Google products are in containers. VMs beat containers in the fact that VMs can use diff OS and kernels while containers must have every container be the same OS and kernel.

Kubernetes is Docker's huge main competitor. And Red Hat?? Containers need to be monitored and controlled so you know what the servers are running.  



HOW TO DEBUG A WEB SERVER

	•	Is the web server started? - You can check using the service manager, also double check by checking process list.
	•	On what port should it listen? - Check your web server configuration
	•	Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
	•	It is listening on the correct server IP? - netstat is also your friend here
	•	Is there a firewall enabled?
	•	Have you looked at logs? - usually in /var/log and tail -f is your friend
	•	Can I connect to the HTTP port from the location I am browsing from? - curl is your friend


FIRST 5 commands to use when you go on a Linux server,
w
history
top
df
netstat

w is a quick summary of every user logged into a computer. top tells us the system summary. gives us server time, uptime, user sessions, load averages, memory usage, tasks, cpu usage and lots of data. df shows the amount of disk space free on the file systems. netstat gives info on the subsystem.



W showers server uptime, which users are connected, and load average which gives us a good measurement of the server health. History shows commands that were previously run by the user and what type of work was previously performed. History is the start of debugging. Top shows what is currently running on the server and orders results by CPU, memory, and utilization. Useful to see what is resource intensive. df shows disk utilization and netstat shows what port and IP my server listens to. What processes is useing sockets, and try netstat -lpn.

MACHINEE


Debugging is about verifying assumptions. Things always fail because nothing is perfect. 
For the machine level, you want to ask yourself these questions:
	•	Does the server have free disk space? - df
	•	Is the server able to keep up with CPU load? - w, top, ps
	•	Does the server have available memory? free
	•	Are the server disk(s) able to keep up with read/write IO? - htop


If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:
	•	free up resources (stop process(es) or reduce their resource consumption)
	•	increase the machine resources (adding memory, CPU, disk space…)
	•	distributing the resources usage to other machines




Network issue
For the machine level, you want to ask yourself these questions:
	•	Does the server have the expected network interfaces and IPs up and running? ifconfig
	•	Does the server listens on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
	•	Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
	•	Does the server have the correct firewall rules? iptables, ufw:
	◦	iptables -L
	◦	sudo ufw status


Process issue
If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).
	•	Is the software started? init, init.d:
	◦	service NAME_OF_THE_SERVICE status
	◦	/etc/init.d/NAME_OF_THE_SERVICE status
	•	Is the software process running? pgrep, ps:
	◦	pgrep -lf NAME_OF_THE_PROCESS
	◦	ps auxf
	•	Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend

https://developer.mozilla.org/en-US/docs/Learn/Getting\_started\_with\_the\_web/How\_the\_Web\_works

Nginx vs Apache. Serves async event driven requests instead of threads. Good performance under high loads. Nginx uses a lot less memory than Apache and handles 4x more requests per second but it is less stable with windows and Apache has full support for Windows. The performance boost comes at a cost of decreased flexibility and requires recompilation when adding modules. But neweer versions have dynamic module loading but some old versions and systems still require static linking.


https://www.tutorialspoint.com/http/http\_methods.htm
https://moz.com/learn/seo/redirection



