#!/usr/bin/python3
from scapy.all import *

# Get user input for the host
host = input("Enter the Host>> ")

print(f"Tracing route to {host}...\n")

for i in range(1, 30):  # Increased TTL range to 30 for better reach
    packet = IP(dst=host, ttl=i) / UDP(dport=33434)

    # Send the packet and wait for a reply
    reply = sr1(packet, verbose=0, timeout=1)

    if reply is None:
        print(f"{i}: *")  # No response, print '*'
    else:
        print(f"{i}: {reply.src}")  # Print the router/hop IP
        
        # If the reply comes from the destination, stop
        if reply.src == host:
            print("Trace complete.")
            break




'''
                                                                     
┌──(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python trace_route.py
Enter the Host>> 45.33.32.156
Tracing route to 45.33.32.156...

1: 10.0.2.2
2: *
3: *
4: *
5: *
6: *
7: *
8: *
9: *
10: *
11: *
12: *
13: *
14: *
15: *
16: *
17: *
18: *
19: *
20: *
21: *
22: *
23: *
24: *
25: *
26: *
27: *
28: *
29: *
              '''
              