#!/usr/bin/python3
import nmap

def nmap_scan(ip_address):
	#create object
	portscanner=nmap.PortScanner()

	open_ports_dict=portscanner.scan(ip_address, arguments="-O -v")

	print("[+] Executing command: ", portscanner.command_line()) 
	open_ports_dict=open_ports_dict.get("scan").get(ip_address).get("tcp")
	print("Open Port--Service")
	port_list=open_ports_dict.keys()

	for port in port_list:
		print(port, "-->",open_ports_dict.get(port)['name'])

	print("-------Operating System-------")
	#get the os of the target host
	os_type=portscanner[ip_address]['osmatch'][0]['osclass'][0]['osfamily']
	print(f"OS Detected: {os_type}")


ip_address=input("Enter IP>> ")
nmap_scan(ip_address)

'''
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python nmap_os.py 
Enter IP>> 127.0.0.1
Open Port--Service
21 --> ftp
22 --> ssh
80 --> http
5432 --> postgresql
-------Operating System-------
OS Detected: Linux
'''