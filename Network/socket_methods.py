#!/usr/bin/python3
import socket

try:
	target=input("Enter target domain name>> ")

	#below provides the name of the PC
	hostname=socket.gethostname()
	print("[+]gethostname: ", hostname)

	#provides the IP address of the PC
	ip_address = socket.gethostbyname(hostname)
	print("Local IP Address: ", ip_address)

	#Get the IP address of a given target domain
	print("gethostbyname: ", socket.gethostbyname(target))
	ip_get=socket.gethostbyname(target)
	print(f"Target domain: {target} has an IP: {ip_get}")

	print()
	#provides IP and full domain name
	print("gethostbyname_ex: ", socket.gethostbyname_ex(target))

	print()
	#get domain name of an IP
	#print("gethostbyaddr: ", socket.gethostbyaddr("50.116.1.184"))

	print()
	#find the fully qualified name of a domain
	print("getfqdn: ", socket.getfqdn(target))

	print()
	print("getaddrinfo: ", socket.getaddrinfo(target, None, 0, socket.SOCK_STREAM))

except socket.error as error:
	print("error occured: ", error)
	print("[+]Connection Error")


'''
When we run the methods we get:
Network>python socket_methods.py
Enter target domain name>> facebook.com
[+]gethostname:  DESKTOP-LSF7UHQ
Local IP Address:  172.29.128.1
gethostbyname:  57.144.138.1
Target domain: facebook.com has an IP: 57.144.138.1

gethostbyname_ex:  ('facebook.com', [], ['57.144.138.1'])


getfqdn:  edge-star-mini-shv-01-mba2.facebook.com

getaddrinfo:  [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 0, '', ('57.144.138.1', 0))]
'''
