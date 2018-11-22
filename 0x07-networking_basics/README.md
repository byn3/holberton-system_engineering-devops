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
unique for each computer connected zzz


