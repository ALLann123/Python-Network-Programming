#!/usr/bin/python3
import nmap

#create an instance of the class
port_scanner=nmap.PortScanner()

#get inputs
print('----------' *6)
print('              Python-NMAP SCANNER')
print('----------' *6)
host_scan=input("Enter the Host IP/Domain>> ")
port_list=input("Enter range to Scan>> ")
option_flag=input("Option Flag(e.g -sS, -sV, -O)>> ")
print("********" *6)
#scan the target
port_scanner.scan(hosts=host_scan, arguments=f"{option_flag} -p {port_list}")

#check the command being executed
print(f"[+]Command Executed {port_scanner.command_line()}")

#save the results in a list
hosts_list= [(x, port_scanner[x] ['status']['state']) for x in port_scanner.all_hosts()]

for host, status in hosts_list: #provide the IP address of the server and whether it is up
	print(host, status)
for protocol in port_scanner[host].all_protocols(): # gets the protocol we are using
	print(f"protocol: {protocol}")
	listport=port_scanner[host]['tcp'].keys()
	for port in listport:
		print('Port: %s State: %s'% (port, port_scanner[host][protocol][port]['state']))

'''
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python range_input.py
------------------------------------------------------------
              Python-NMAP SCANNER
------------------------------------------------------------
Enter the Host IP/Domain>> scanme.nmap.org
Enter range to Scan>> 22-80
[+]Command Executed nmap -oX - -n -p22-80 scanme.nmap.org
45.33.32.156 up
protocol: tcp
Port: 22 State: open
Port: 80 State: open
'''