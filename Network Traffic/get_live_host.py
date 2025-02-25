#!/usr/bin/python3
from scapy.all import *

print("******************Check LIVE IP***************")
target=input("Enter the target IP>> ")

# create a ping packet and send to the target
icmp=IP(dst=target)/ICMP()

#receive the response of the ping in a variable
recv=sr1(icmp,timeout=10)

if recv is not None:
	print()
	print(f"[+]The target: {target} is LIVE!!")
else:
	print()
	print(f"[+]{target}is down!!")

'''
(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python get_target_status.py  
******************Check LIVE IP***************
Enter the target IP>> 167.82.44.223
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets

[+]The target: 167.82.44.223 is LIVE!!
'''
  