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

