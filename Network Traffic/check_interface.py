#!/usr/bin/python3
import pcapy
import datetime

#get the interfaces onthe device
interfaces=pcapy.findalldevs()

print("[+]Available Interfaces...")
#print the available interfaces
for interface in interfaces:
	print(interface)

'''
┌──(myenv)─(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python check_interface.py
[+]Available Interfaces...
eth0
any
lo
bluetooth-monitor
nflog
nfqueue
dbus-system
dbus-session
                       
'''

