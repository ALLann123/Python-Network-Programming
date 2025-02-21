#!/usr/bin/python3
import socket

ip=input("Enter target IP>> ")

#create a list of target ports

portlist=[21,22,23,80]

for port in portlist:
	#create a socket object
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#try connecting to the socket using ip and the port specified
	result=sock.connect_ex((ip,port))
	if result==0:
		print(port,":","Open")
	else:
		print(port, ":", "Closed")
	#print(port, ":", result)
	sock.close()

'''NOTES
J:>python socket_open_ports.py
Enter target IP>> scanme.nmap.org
21 : 10061
22 : 0
23 : 10060
80 : 0
When the status is 0 its opened else a number its closed

Using if statement :
>python socket_open_ports.py
Enter target IP>> scanme.nmap.org
21 : Closed
22 : Open
23 : Closed
80 : Open'''