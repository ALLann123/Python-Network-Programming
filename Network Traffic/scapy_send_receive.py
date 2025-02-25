#!/usr/bin/python3
from scapy import *

target=input("Enter website>> ")
packet=Ether()/IP(dst=target)/TCP(dport=80, flags="S")
packet.show()

srp1(packet, timeout=10)
print(srp1)

'''
─(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python3 scapy_send_receive.py
Enter website>> www.python.org
###[ Ethernet ]###
  dst       = None (resolved on build)
  src       = 08:00:27:6c:9c:2a
  type      = IPv4
###[ IP ]###
     version   = 4
     ihl       = None
     tos       = 0x0
     len       = None
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = tcp
     chksum    = None
     src       = 10.0.2.15
     dst       = Net("www.python.org/32")
     options   \
###[ TCP ]###
        sport     = ftp_data
        dport     = http
        seq       = 0
        ack       = 0
        dataofs   = None
        reserved  = 0
        flags     = S
        window    = 8192
        chksum    = None
        urgptr    = 0
        options   = []

Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
<function srp1 at 0x7fa172ad99e0>
'''
