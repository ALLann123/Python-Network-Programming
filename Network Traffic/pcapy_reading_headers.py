#!/usr/bin/python3

import pcapy  # Library for packet capture
from struct import unpack  # Used for unpacking binary data

# Get available network interfaces
interfaces = pcapy.findalldevs()
print("[+] Available Interfaces:")
for interface in interfaces:
    print(interface)

# Prompt user to select an interface for sniffing
interface = input("Enter interface name to sniff >> ")

# Open the selected interface for packet capturing
# 65536 - Maximum bytes to capture per packet
# 1 - Enable promiscuous mode
# 0 - No timeout (capture indefinitely)
cap = pcapy.open_live(interface, 65536, 1, 0)

while True:
    # Capture a packet
    (header, payload) = cap.next()
    
    # Extract Layer 2 (Ethernet) header (first 14 bytes)
    l2hdr = payload[:14]
    l2data = unpack("!6s6sH", l2hdr)
    
    # Extract Source and Destination MAC addresses
    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2data[1][0], l2data[1][1], l2data[1][2], l2data[1][3], l2data[1][4], l2data[1][5])
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2data[0][0], l2data[0][1], l2data[0][2], l2data[0][3], l2data[0][4], l2data[0][5])
    
    print(f"Source MAC: {srcmac}")
    print(f"Destination MAC: {dstmac}")
    
    # Extract Layer 3 (IP) header (next 20 bytes from offset 14)
    ipheader = unpack('!BBHHHBBH4s4s', payload[14:34])
    timetolive = ipheader[5]  # Time To Live (TTL)
    protocol = ipheader[6]  # Protocol type
    
    print("Protocol:", str(protocol), "Time to Live:", str(timetolive))
'''
                                                                                
┌──(myenv)─(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python pcappy_reading_headers.py
[+] Available Interfaces:
eth0
any
lo
bluetooth-monitor
nflog
nfqueue
dbus-system
dbus-session
Enter interface name to sniff >> eth0
Source MAC: 08:00:27:6c:9c:2a
Destination MAC: 52:54:00:12:35:02
Protocol: 1 Time to Live: 64
Source MAC: 52:54:00:12:35:02
Destination MAC: 08:00:27:6c:9c:2a
'''