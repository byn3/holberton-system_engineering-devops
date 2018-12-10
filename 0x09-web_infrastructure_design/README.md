

You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
Okay.


You must be able to explain what are each components doing.
Gotcha.



You must be able to explain system redundancy
Explain system redundancy.



Know all the mentioned acronyms: LAMP, SPOF, QPS
LAMP is Linux as the OS, Apache as the HTTP server, mySQL as the relational database management system, and PHP as the programming language.

SPOF is Single Point Of Failure. Or Strategic Plan for Ontario Fisheries.

QPS is queries per second. 



NOTES



NETWORK



Networking is a big part of what made computers so powerful and why the Internet exists. It allows machines to communication between each other.

netowrk protocol is a set of rules that says how to format, transmit, and receive data so computer devices can communicate. Network protocols are common language. All networks end users rely on these protocols for connectivity.

Network protocols break large into small. The standard model is the OSI, open systems interconnection. 

A set of cooperating network protocols is the protocol suite. TCP/IP suite includes numberous protocols that work together.
TCP is transmission control protocol and that exchanges messages with other internet points at the packet level. IP is internet protocol and those are rules that send and recieve messages at the internet address level.
HTTP is hypertext transfer protocol and FTP file transfer protocol which has their own sets of rules.
Networks have 3 types of protocols, communication (like ethernet), management (like simple network management protocol SNMP) and security (secure shell SSH).
Many network protocols dall into many defined tasks like authentication, automation, correction, compression, error detection, file retreival, file transfer, limk aggregation, routing, sematics, syncronization, and syntax. 

TCP/IP notes refer to other project.




SERVER

Servers are located in datacenters which are buildings hosting hundreds, or thousands of computers (servers). You can think of a server as a computer without keyboard, mouse, screen, that is accessible only by network. A server can be physical or virtual. A server runs an OS (operating system).

A server is a device or program that provides stuff for clients. Database servers, file servers,. mail servers, web servers, and game servers.

Servers are not web servers. Today, client-server systems are mostly request-response models.
CPU, memory, hard drive space is big for servers. Server applies to physical and virtual. Virtual servers are just servers on the physical device.
They created instances on 1 physical system.

Server operating system. A server's OS provides services to users. Services servers provide are directory servers (access to info and stuff, has permissions), DNS or dynamic name service (the translator for domain name to IP address, translate friendly name to IP number), file server (stores files), index search service (inventories all files and does search queries), proxy server (it is middle man and used for security. traffic cop), web server (provides service for hosting and managing websites. sites acced by browsers), database service (collection of info), email service (provides users with ability to send, receive, and review email), management server (allows admin to monitor and resolve issues), firewall service (security, website access list) print service (printers, queues, administer printers), virtualization service (allows multiple instances o a server to be run on a single physical system, very power hungry. needs to cool, maximixes efficiency). 

Server operating systems. Microsoft is 75% of servers, apache is 350 million sites (prob 65% market), linux is most versatile server. Microsoft is good to get a job. Big chunk of market.

Data centers hold thousands of machines. A rack has lots of small computers. Has servers, 1 U. U for unit and install to the rack. All racks need internet connection and power. Lots of cooling units and fans. Need to reduce cooling cost. Go to cold weather or cheap power. 





WEB SERVER


Software that delivers a web page. A server can be a physical machine or actual computer but todaty with the cloud, a virtual computer can be a VM or container.

A webserver processes incoming network requests over HTTP and other protocols. Primary functions are to deliver, store, and process web pages to clients.
There also needs to be ways to recieve content from clients which is like submitting web forms and uploading files.

PHP is hypertext preprocessor. A scripting language. Web servers are not just for the web, it can also be embedded in devices that use the internet, like printers, routers, webcams, and other stuff.

Apache is a leading web server. Other popular ones are Microsoft's Internet Information Server, IIS and nginx from NGNIX. There is also Google Web Server, GWS, and IBM's Domino.
Considerations to choosing which is how well it works with the OS and other servers, the abilithy to handle server side programming, security, and the tools that come with it.


DNS

The tech that translates domain names to machine adapted IP.
Domain Name System. Check DNS, then OS, then if OS fails... RESOLVER. Browser and OS both searched their cache to see if they know the IP for EXAMPLE.COM but since they did not the OS is calling a resolver.
Resolver server is usually the ISP. All resolvers must know where the root server is. If the resolver don't know shit then it will locate the root and the root server knows where to find the .COM TLD server. TLD stands for top level domain. Root tells the resolver where to look and the resolver will save this info so it doesn't have to ask root.
Root servers are 13 total server that sit at the top of DNS. Root has .COM, .ORG, .NET. All of these are scattered around the world and operated by 12 other organizations. They are names [letter].root-servers.net and letter ranges from a to m.
The coordination of most top level domains (TLD) belong to the Internet Corporation for Assigned Names and Numbers (ICANN). .COM was TLD was one of the first created in 1985. It is the largest. There are other TLDs like country TLDs like .jp or .uk or .fr. There are internationalized country code TLDs like .zhoneguo (but the characters) and also generic TLD, .net, .org, .edu. 

There are infrastructure TLDs like .arpa and those are used for reverse DNS. They are given an IP and will look up the domain. Lots of new TLDs are being made like .app and .health and .hot.

How does the .com domains make a connection? It uses help with Domain Registrars. When a domain is purchased, the domain registrar reerves the name and communicated to the TLD registry the authoritative name servers. 

Usually more than 1 name server attacked to a domain. It helps distribute the workload and the DNS zone availabiltiy is increased. In cases of a failure, this is good reliability. If you want to know who are the authoritative name servers for the domain, run a WHOIS query and the computer needs that tool to run it. 

Authoritative name servers will give the IP to the resolver and it will save it. Root tells resolver where to find the .COM server and the TLD server gave the authoritative name servers' addresses. Then the auth server gave the IP address and the resolver will give back the IP to the browser.

The main DNS record types are A, CNAME, MX, and TXT.

A record maps a domain name to IP address IPv4. A stands for address.
CNAME is canonical name record. It maps one domain to another which is convienent when running multiple services like an FTP and a webserver. CNAME records must always point to another domain name and never directly to an IP address.

MX records stands for mail exchanger record. It is a type of certified and verified resource record in DNS. It specifies the mail server responsible for accepting email messages and preferences for prioritizing mail if multiple servers are available. Email should be routed with the SMTP (simple mail transfer protocol).

Lowest numbered records are most preferred (RFC 5321), smaller distances are more prederable. Load distribution among the array of mail servers is to return the same preference number for each server in the set. 

TXT record is short for text record. It provides the ability to associate text with a host or other info. Common uses include verification of domain ownership, domainKeys, and 0 configure networking DNS-based service discovery.

Round Robin DNS is load balancing multiple internet services like web servers and email servers. It creates multiple DNS. Do it by configuring the DNS server to send a list of IP addresses of several servers with the same hostname. Eg. example.com can return 2 IP addresses 202.54.1.2 and 202.54.1.3. All clients would recieve service from the two different servers randomly distributed and that would distribute the overall load.

Use round robin DNS for load distribution, load balancing, and fault-tolerance service. https://www.dnsknowledge.com/whatis/round-robin-dns/



Root domain is the parent to a sub and its name can not be divided by a dot. Domain providers allow mydomain.com but will ban my.domain.com. Domain providers block the ability to create a root domain until a name without a dot is given. Why?

The dot delimits the subdomain name. The admin can make any number of subdomains and that would mean for domain.com, he or she can make my.domain.com and your.domain.com and yea... creating multiple subdomains is free and does not require setting up new accounts on domain provider sites.


www is a subdomain. www always leads to the main domain.






LOAD BALANCER


Balancers will distribute the work load of the system to multiple individual systems. This increases reliability, efficiency, and availability.
PROS: Reduce workload on an individual server, can allow for vast amounts of work to be done concurrently, faster responses, no single point of failures, efficient and optimal use of resources, scales (increase or decrease number of servers without being offline), reliability, and security. Physical servers and IPs are abstract in some cases.

2 types of load balancers, software and hardware.
Software implements 1 or more scheduling algorithms. These 3 are the basic ones and most modern balancers use a combination of these to set a trade off with difference goals.
1\) Weight scheduling algo. Work is assigned according to a weight. Each server gets an assigned weight depending on hardware capabilities and the load balancer will compute the percentage of traffic to be sent to a certain server.
This weight scheduling is used when there is a big difference between the capabilities and specs of the servers present in the farm or cluster.
This is efficient in managing the load without swarming the low capacity servers. It most efficiently utilizes the available server resources. Software load balancers consumes the processor and memory of servers. Hardware balancers are specialized in between server and client. It can be a switch or router hardware or a specialized machinne.
2\) Round Robin Scheduling. Requests are served in sequential order and it cycles. If the servers are equal then this is fine.
3\) Least Connection First Scheduling. Requests are served to the server that has the least number of connections. This algo is used when we have large number of connections that are unevenly distributed and this is usually coupled with sticky session or session aware load balancing. All the requests is sent to the same server to maintain the session state. This approach is used when we have session aware write operations in sync with client and the server. This will avoid inconsistencies and we can have smart implementation of the combos of the above.


We can have Weighted round robins or Weighted least connection scheduling. Hybrid scheduling has evolved to use more combos or variations.

Examples of software load balancers is HAProxy for TCP load balancing, NGINX for http load balancing with SSL termination support, mod\_athena for apache based http loads, Varnish for reverse proxies, balance for open source TCP loads, LVS for linux virtual server offering 4 load balacing.

Hardware load balancers
Specialized routers and switches are deployed between servers and clients. It is implemented on Layer 4 (transport) and Layer 7 (application) of OSI model. They are called L4-L7 routers.

Layer 4 uses TCP, UDP, and SCTP protocol details to make decisions on which the server the data is sent to. Most Layer 4 balancers are NATs or network address translators. This shares the load to different servers and the routers hide multiple servers and rtranslate all response data packets. DNS load balacing picture!!

Direct routing, Tunnel or IP tunneling. Layer 7 Hardware Load Balacing. Forms a ADN or application delivery network. Languages are filteres to specific servers. URL parsing, Cookie sniffing, HTTP reading. more here https://www.thegeekstuff.com/2016/01/load-balancer-intro/


F5 BIG-IP load balancer. CISCO system catalyst. Barracuda load balancer. Coytepoint load balancer. 






LOAD BALANCING ALGOS
https://devcentral.f5.com/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms





MONITORING

Software monitoring watches computer metrics, records them, and emits alarms when something is unusual. You cannot fix or improve what you cannot measure.

Web stack monitoring can be broken down into 2 categories which are application moitoring which gets data about the running software and making sure it is working, and also server monitoring which gets data about virtual or physical server and makes sure they are not overloaded. It can be overloaded by CPU, memory, disk spac or network overload.

Famous tools are NewRelic, DataDog, Uptime Robot, Nagios, WaveFront. https://intranet.hbtn.io/concepts/13










Problem 0:



What is a server
A computer or device that connects and accesses a network.


What is the role of the domain name
Used to identify one or more IP addresses.

What type of DNS record www is in www.foobar.com
A record? it is a subdomain. 

What is the role of the web server
Sends back web content.

What is the role of the application server
Web apps or desktop apps run in application servers. Application servers have web server connectors, programming languages, runtime libraries, database connectors, and admin code that deploys, configures, manages, and connects the components on a web host. 

What is the role of the database
Creation and management of data. Without it running and managing data is impossible.

What is the server using to communicate with the computer of the user requesting the website
Web server.

You must be able to explain what are the issues with this infrastructure:
SPOF
If one server and that fails. It all fails. Need multiple. Need clusters.
Also just one network switch is bad. That 1 switch is the SPOF. All servers connected to that switch would be inaccessible if the switch goes out. 

Downtime when maintenance needed (like deploying new code web server needs to be restarted)
If there is only one instance of a server and we need to take it down, that is shitty work. We need multiple to ensure reliability.


Cannot scale if too much incoming traffic
If there is too much traffic then we good buisness. If we cannot scale then we have bad load balancers or not enough servers. We need to buy more.









PROBLEM 1


You must be able to explain some specifics about this infrastructure:
Okay.


For every additional element, why you are adding it
To do stuff and trade offs.


What distribution algorithm your load balancer is configured with and how it works
Hybrid of the 3 algos.


Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both

Active-Active prob. But active passive is better. 

2 or more servers aggregate network traffic and work as a team to distribute the traffic onto the servers. Bad tradeoff of this is near full capacity and if we go over or something breaks then we have user sessions timing out or running slow.

Active-Passive is configuring to H/A mode and traffic is offloaded to the most suitable server. 
The other load balancer will be in listen mode and constantly monitor the performance of the primary, ready to always step in and take over the load if the primary is having issues or failing. 
Uninterrupted service for customers is achieved with this model and we can deal with planned or unplanned service outages. active passive is best if we need a 24/7 connection. 



How a database Primary-Replica (Master-Slave) cluster works
When a primary fails, one of the secondaries will automatically be the new primary and i have no clue.


What is the difference between the Primary node and the Replica node in regard to the application
???


You must be able to explain what are the issues with this infrastructure:

Where are SPOF
A lot of places?

Security issue (no firewall, no HTTPS)
Hackzorz./

No monitoring
Cant find problems if no monitoring.







PROBLEM 2


You must be able to explain some specifics about this infrastructure:

For every additional element, why you are adding it

What are firewalls for
Prevent unauthorized acces to or from a computer network.


Why is the traffic served over HTTPS
Encryption. Secure. Protects sensitive info. No data loss. Increases trust and confidence. 


What monitoring is used for
Need to have data to fix or improve things
https://www.quora.com/What-are-considered-best-practices-when-monitoring-a-web-server


How is the monitoring tool collecting data
Data points.


Explain what to do if you want to monitor your web server QPS
Use a tool. https://www.quora.com/How-can-I-calculate-how-many-requests-per-second-my-server-can-handle


You must be able to explain what are the issues with this infrastructure:

Why terminating SSL at the load balancer level is an issue
Okay. https://serversforhackers.com/c/so-you-got-yourself-a-loadbalancer


Why having only one MySQL server capable of accepting writes is an issue
Only one server in general is bad. Need more.


Why having servers with all the same components (database, web server and application server) might be a problem

Waste of resources and memory.
