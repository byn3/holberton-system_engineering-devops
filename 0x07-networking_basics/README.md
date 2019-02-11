# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---  

## Networking basics  
Notes taken at the end of this README.  

## Each scripts and their output?**  
* Script 0 - Quiz.      
* Script 1 - Another quiz.    
* Script 2 - Another another quiz.      
* Script 3 - Another another another quiz.    
* Script 4 - Write a Bash script that displays listening ports.    
* Script 5 - Write a Bash script that pings an IP address passed as an argument.      



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



### My notes  
___

OSI model  
Open systems interconnection is a reference model for how apps communicate over
a network.  

OSI model layers. The main concept of OSI is that the processes of
communication between 2 endpoints in a network are divided into 7 layers. Data
flows through these 7 layers.  

Layer 7: Network process to app, 6: Data representation and encryption, 5:
Interhost communication, 4: End-to-end connections and reliability, 3: Path
determination and IP, 2: MAC and LLC (physical addressing), 1: Media, signal,
and binary transmission.  

The 7 layers are made up of OS, netword card evice drivers, networking
hardware, and other wireless protocols.   

Layer 7: The application layer. This layer is where communication partners are
identified.  

Layer 6: This is part of the OS and converts incoming and outgoing data from
one format to another. From clear to encryped text to send or receive encrypted
text and put it in clear text.  

Layer 5: The sessions layer. This coordinates and terminates conversations.
It authenticates and reconnects. The TCP (Transmission Control Protocol) and
UDP (User Datagram Protocol) provides these services.  

Layer 4: The transport layer. This layer manages packets of data and delivery
of them. It checks for errors when the data arrives. The internet's TCP and UDP
provides these services for most apps.  

Layer 3: The network layer. This handles addressing and routing the data.
Handles the right destination. IP is the network layer for the internet.  

Layer 2: The data-link layer. This sets up links across the physical network,
putting packets into network frames. 2 sublayers in this and those are the
logical link control layer and the media access comtroll later (LLC and MAC).
MAC includes ethernet and 802.11 wireless.  

Layer 1: The physical layer. This layer conveys the bit stream across the
network either electronically, mechanically, or through radio waves. This layer
covers many devices like cabling, connectors, tranceivers, receivers, and
repeaters.  



use man netstat and man ping for more info on OMG THIS IS TOO MUCH STUFF TO
READ ON 1 DAY.  


Intro to area networks.  
WAN (Wide Area Network), LAN (Local Area Network), WLAN (Wireless Local Area
Network), MAN (Metropolitan Area Network), San (Storage Area Network/ Small
Area Network/ Server Area Network/ System Area Network), CAN (Campus Area
Network), PAN (Personal Area Network).  

Most popular are LAN and WAN. LAN is local area network. It connects network
devices over short distances. Offices, home, schools etc. In TCP/IP networking
a LAN is often a single IP subnet. LANs are usually owned and controlled by a
single person or organization and use ethernet or Token Ring.  

WAN is wide area network. WAN is a large physical distance. The internet is the
biggest WAN. WAN is dispersion of collection of LANs. A router connects LANs to
WANs and the router maintains both a LAN and WAN address. Differences of WAN
from LAN are so: no one person owns it. Many people have distributed ownership
of it and they use technologies like ATM, frame relay, X.25.  


Usually residences have 1 LAN and connect to the internet WAN with an ISP
(internet service provider) using a broadband modem. The ISP provides a WAN IP
to the modem and all computers use the LAN private IP addresses. Computers on
the LAN can communicate directly to each other but must go through the router
to reach the ISP.  


Ethernet and Wifi are 2 main ways to enable LAN connections. Wifi uses radio
waves. Other methods exist like token ring, fiber distributed data interface,
and ARCNET. These have lost popularity due to the speed increases in wifi and
ethernet. A LAN server can be used as a web server if enough security if
implemented. Wifi is a growing king due to the number od mobile devices. WLANS
growing too much.   

WAN connects multiple LANs. A WAN can connect a companies headquarters with its
branch offices. Usually a router connects LAN to WAN.   


VPN (Virtual Private Network) facilitates connectivity between WAN sites. IPsec
VPN is common for continuous open site to site connections, eg. between office
branches. SSL VPN is the preferred choice for enabling remote access for
individual users because the data transmitted from users across the WAN is
encrypted. Direct fiber optic links are used to connect sites on a WAN. Fiber
optics are better. They are more reliable and secure than VPNs but they are
costly.  


Wired WANs can include multiprotocol label switching, T1s, carrier ethernet, an
commercial broadband internet links. Wireless WAN tech can include cellular
data like 4G and public wifi or satellite networks.  

WAN infrastructure can be privately owned or leased as a service from a third
party service provider, like from a telecommunications carrier, ISP, or cable
company.   

SD-WAN is software defined WAN which is designed to make hybrid WANs. CPE is
customer premises equipment. SD-WANs, CPEs, and software platforms provide 2
functions: they aggregate multiple public and private WAN links and they select
the most optimal path for traiffic, automatically.  

WAN optimization. Latency and bandwidth constraints cause WANs to suffer with
performance. We can optimize WAN with techniques including deduplication,
compression, protocol optimization, traffic shaping, and local caching.   



What is a MAC address?  

NIC is a network interface card which is a circuit that makes it possible for a
computer to connect to a network. NIC turns data into electric signals that can
be transmitted ofer a network.  

Every NIC has an address known as a Media Access Control or MAC. IP addresses
are associated with TCP/IP, MAC is linked to network adapters. When an adapter
is manufactured, a MAC address is given. MAC address is hardcoded into the NIC
card and is unique. ARP (Address Resolution Protocol) will translate an IP
address into a MAC address. The ARP is like a passport that takes data from an
IP address through hardware.  

The MAC is the hardware address. It can be referred to as the networking
hardware address or the burned-in address (BIA) or the physical address. MAC
addresses is usually a six sets of 2 digit characters or digits seperated by
colons. Some NICs have a OUI or organized unique identifier which are the first
3 octets. Dell is 00-14-22 and cisco is 00-40-96.  

All devices on the same network have diff MAC addresses and MAC addresses are
useful in diagnosing network issues, especially problems with IP addresses.  

MAC addresses do not change and dynamic IP addresses can so a network
administrator can rely on the MAC.   

For security on wireless networks, a process called MAC filtering prevents
unwanted network access by hackers and intruders. Filtering works by having the
router configured to accept traffic only from very few specified MAC addresses
and in this way, only approved MAC addresses can get into the network.  


All machines on the internet have a unique IP address which acts like a
telephone number.  

IPv4 vs IPv6. Most of today is IPv4 which is internet protocol version 4 which
uses 32 bit addresses which means there is a limit of 4.2 billion. Due to
growth, we ain't got enough of this shit. Internet protocol version 6 will
allow 128-bit addresses instead of 32 which is fucken huuuuge. Only problem is
that we need to upgrade people's shitty routers and hardware.  

The info here and on will cover mainly IPv4 due to basic bitches and
simplicity. The IPv4 is still very common. The address consists of 4 numbers
separated by periods and the numbers are 0 to 255 (eg. 192.168.1.10). This is
called decimal notation.  

There are 3 special IPs. 0.0.0.0 is the default network. 255.255.255.255 is the
broadcast address which is used for routing. The last special one is 127.0.0.1
which is a loopback address or your own machine. Typing in http://127.0.0.1
will try to connect to your own computer and you will get an error unless you
are running a web server.  

Some guidelines to how IP addresses can look. The 4 numbers must be between 0
and 255. IP addresses of 0 or 255 repeating is reserved. IP addresses must be
unique for each computer connected. If 2 computers have the same IP address, an
IP conflict occurs and they cannot communicate with each other.  

IP address classes. Class A is 0 to 126. B is 128 to 191. C is 192 to 223. D is
224 to 239. E is 240 to 255. 127 is skipped from class A to B because of
loopback addresses. Loopback targets your own computer and is useful for
testing and debugging. The rest of the IP addresses are reserved for companies or
orgs.  

0.0.0.0 is default network which is for general routing. Class A is for the 126
networks that are usually the largest multi-national companies. Class B is
usually for ISPs and major netowrks like college or hospitals. Class C is for
smal to midsize companies. Class D is for a service called multicast. Class E
is for experimental use. Broadcast is 255.255.255.255 which is used to
broadcast messages to the entire network.  

Private addresses. 10 for class A. 172 for class B. 192 for C. These are for
internal use for companies or homes. These are for networks that waant to use
TCP/IP but do not want to be visible on the internet.  

Common problems and resolutions. One is assigning an IP that is already
assigned. Most OS will give a IP conflict warning and that is caused by one
device detecting another one on the same network using the same address.  

The best solution is to use a service called DHCP and most home routers provide
this. DHCP is dynamic host configuration protocol and that assigns addresses to
devices. You tell the DHCP what range of IP addresses you want and it handles
the rest.  

Public IP addresses can be accessed over the internet and is globally unique.
Private IP addresses is for stuff you want to hide from the Internet. The
router will get the public IP and each of the private IP via DCHP protocol.  

IANA is internet assigned numbers authority. IANA is an org that registers IP
addresses to orgs and ISPs. The InterNIC is the inernet network information
center and they reserve certain address blocks for private use. The private IP
addresses are 10 for A, 172 for B, 192 for C.  

To allow direct access to a local priovate device, a NAT (Network Address
Translator) is needed.   


TCP is transmission control protocol. This establishes virtual connections from
a source to a destination. IP is internet protocol. IP specifies the
technical format of packets and the address scheme. IP is like a postal address
where you can drop off mail but there is not a direct link. TCP/IP is a
connection so messages can be sent over a breif period of time.   

The benefits of IPv6 is no more NAT (Network Address Translation), auto
configs, no more private address collisions, better routing, simpler header
format, flow labeling, built in authenticator and privacy, flexibility, easier
administration, no more DHCP.   



TCP and UDP are 2 protocols for different tyoes of data. TCP/IP is for devices
to talk over the internet. TCP delivers and recieves and error checks data
packets. UDP is user Datagram Protocol. That is faster by disregarding error
checking. Packets are bits of data. They are sent throug hthe internet.  

TCP is the most common. When I request a web page in a browser, the computer
sends the TCP packets to a web server's address. The web server will send the
web page back via a stream of TCP packets. The web browser stiched together the
packets to form the web page. Any action on a site from signing up to clicking
links to posting comments will get the browser to send TCP packets to a server
and the server will send packets back.  

TCP is all about reliability. The packets are tracked so no data is lost or
corrupted, even if a network fucks up. If the recipient is offline then the
computer just gives up and the error message is can't communicate with remote
host.  

TCP orders packets by numbering them. It also error checks by having the
recipient send a response back saying message was recieved. If the response is
not right, the packet can be resent.  

Process explorer and other system utilities can show the types of connections a
process makes.  

UDP works similar to TCP but no error checking. Latency increases with the back
and forth error checking. But UDP just sends the next packet and if some are
lost then oh well. This is very fast way of communication. UDP is meant for
speed and not accuracy. This is the go to for online games and live
broadcasting.   

Twitch or live streams are UDP. There is a constant stream of UDP packets to
computers watching and if connection is lost for a few seconds, the video
freezes or gets jumpy and then will skip to the current. Minor packet loss
causes video or audio distortion as videos continue to play without data.  

In online games, this is the same. Missing some UDP packets can cause player
characters to teleport around. LAG. So whether an app uses TCP or UDP is up to
the developer and what the app needs. Most apps need error correction but
others need speed and reduced overhead.   

This knowledge most affects netword admins or software developers. If you don't
know if an app used TCP or UDP you can generally select both.  


https://en.wikipedia.org/wiki/List\_of\_TCP\_and\_UDP\_port\_numbers  


Ping is a computer network administration software utility used to test if a
host is reachable on an IP netowrk. It measures round trip time. Ping uses ICMP
or internet control message protocol echo request packets. The program will
report errors, packet loss, and stats. The CLI or command line ping will vary
due to size of payloads, number of tests, and other options. There is a ping6
for testing IPv6.  

Positional parameters. Useful for bash scripts. $stuff. $#. $numbers. $\*. $@.
Shift. Loops. Mass usage. Range.   


### More notes!
___

At the end of this project you are expected to be able to explain, without the help of Google:  

OSI model   

What it is?  
Open systems interconnection model. Explains how a computer or network can communicate. Standardizes communication between computers.  

How many layers does it have?  
7  

How it is organized?  
Application, Presentation, Session, Transport, Network, Data Link, Physical.  
https://www.webopedia.com/quick\_ref/OSI\_Layers.asp  

What is a LAN?  
Local Area Network.  

Typical usage
Connects a computer to a home or office network and devices on a LAN can access data from any machine connected to the network.
Typical geographical size.
Home or office. Small I guess.  

What is a WAN?  
WAN is a wide area network.
Typical usage
It connects multiple LANs over a wide area.
Typical geographical size
Huge. It can connect headquarters, branches, offices, clouds, etc.  

What is the Internet?  
I don't know. Fucken magic?? It is a wide ass network that lets computer networks around the world run by governments, companies, universities, and other orgs talk to each other. It is a mass of cables, computers, data centers, routers, and a bunch of tech. 5 exabytes of data goes through the internet each day.  

IP address, what is it?  
Like a postal address for your computer.
What are the 2 types of IP address
IPv4 and IPv6. Version 4 and 6.  

What is localhost?  
Local host is your own computer. Loopback.  

What is a subnet?  
Subnetwork? It is a network inside a network. Breaking a large network into smaller ones. Delivers data efficiently. Subnets are like a mailroom. Subnets are the next tier of logical organization. IPs break down into the network ID and the the host ID. Smart pickles borrow some bits of the Host ID to create a subnet address like a subnet mask.   

Why IPv6 was created?  
Cause IPv4 will not be able to hold everything.  
TCP/UDP
What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
TCP and UDP. One favors error checking and the other favors speed.
What is the main difference between TCP and UDP  
Error checking.
TCP/UDP Ports  

What is a port?  
A place where boats dock. HA. I'm so funny. A port is an endpoint of communication. A port is a specific process or a network service. A port is associated with an IP address and the protocol type. A port number is a 16 bit unsigned number and it is the network address of a message. 
Memorize SSH, HTTP and HTTPS port numbers
NOPE. THANK YOU. NEXT.  

What tool/protocol is often used to check if a device is connected to a network?
Ping baby.
