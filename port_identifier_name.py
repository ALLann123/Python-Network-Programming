#!/usr/bin/python3
import socket
import sys
def find_service_name():
	while True:
	    try:
	        # Prompt the user to enter a port number
	        print("****************************************")
	        print("type exit to close!")
	        user_port = input("Enter a port number>> ")

	        if user_port == "exit":
	        	sys.exit()
	        else:
	        	user_port=int(user_port)
		        # Get the service name for the provided port using TCP
		        service_name = socket.getservbyport(user_port, 'tcp')
		        print(f"Port: {user_port} => Service name: {service_name}")
	    
	    except ValueError:
	        print("Invalid input! Please enter a valid port number.")
	    except OSError as error:
	        print(f"Port {user_port} is not valid or the service is unknown: {error}")

# Execute the function
find_service_name()




'''
─(root㉿kali)-[/home/kali/python/network]
└─# python port_name.py
====================================================
Enter a port number: 40
Port 40 is not valid or the service is unknown: port/proto not found
====================================================
Enter a port number: 21
Port: 21 => Service name: ftp
====================================================
Enter a port number: 22
Port: 22 => Service name: ssh
====================================================
Enter a port number: 23
Port: 23 => Service name: telnet
====================================================
Enter a port number: 25
Port: 25 => Service name: smtp
====================================================
Enter a port number: 80
Port: 80 => Service name: http
====================================================
Enter a port number: 443
Port: 443 => Service name: https
====================================================
Enter a port number: 3389
Port: 3389 => Service name: ms-wbt-server
'''