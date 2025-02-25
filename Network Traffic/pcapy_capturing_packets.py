#!/usr/bin/python3
import pcapy
import datetime

#get the interfaces onthe device
interfaces=pcapy.findalldevs()

print("[+]Available Interfaces...")
#print the available interfaces
for interface in interfaces:
	print(interface)

#select prefered interface to sniff from
selected_interface=input("Enter interace to sniff: ")
print("Selected Interface: "+selected_interface)

#we begin capturing packets
cap=pcapy.open_live(interface, 65536, 1, 0)
while True:
	(header, payload) = cap.next()
	print(f"[+] {datetime.datetime.now()}: captured %d bytes", header.getlen())


'''
(myenv)─(root㉿kali)-[/home/kali/python/traffic_sniffing]
└─# python pcappy_packet_capture.py 
[+]Available Interfaces...
eth0
any
lo
bluetooth-monitor
nflog
nfqueue
dbus-system
dbus-session
Enter interace to sniff: eth0
Selected Interface: eth0
[+] 2025-02-25 10:07:17.548706: captured %d bytes 169
[+] 2025-02-25 10:07:17.548816: captured %d bytes 198
[+] 2025-02-25 10:07:17.548848: captured %d bytes 200
[+] 2025-02-25 10:07:17.549140: captured %d bytes 192
[+] 2025-02-25 10:07:17.567951: captured %d bytes 189
'''
