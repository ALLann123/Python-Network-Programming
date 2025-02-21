#!/usr/bin/python3
import socket

def find_services_name():
	try:
		user_port=int(input("Enter a port>> "))
		for port in [21,22,23,25,80,user_port]:
			print("Port: %s => service name: %s"%(port, socket.getservbyport(port,'tcp')))
			#print("Port: %s => service name: %s"%(53, socket.getservbyport(53,'udp')))
	except OSError as error:
		print("PORT NOT VALID!!: ", error)

#execute function
find_services_name()

'''
Use the above idea to build a learning script of whatever port and service running onthem
Network>python service_names.py
Port: 21 => service name: ftp
Port: 53 => service name: domain
Port: 22 => service name: ssh
Port: 53 => service name: domain
Port: 23 => service name: telnet
Port: 53 => service name: domain
Port: 25 => service name: smtp
Port: 53 => service name: domain
Port: 80 => service name: http
Port: 53 => service name: domain

with user input
Network>python service_names.py
Enter a port>> 443
Port: 21 => service name: ftp
Port: 22 => service name: ssh
Port: 23 => service name: telnet
Port: 25 => service name: smtp
Port: 80 => service name: http
Port: 443 => service name: https

'''
