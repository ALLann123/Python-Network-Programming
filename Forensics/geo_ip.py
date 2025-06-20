#!/usr/bin/python3
import socket
from geoip import geolite2
import json

ip_address=input("GET IP Geolocation>> ")

def main(ip_address):
	#get the IP address if domain
	ip_address=socket.gethostbyname(ip_address)

	print(f"[+]Domain IP translates to: {ip_address}")

	#get geolocation information
	geolocation=geolite2.lookup(ip_address)

	if geolocation is not None:
		print('Country: ', geolocation.country)
		print('Time zone: ', geolocation.timezone)
		print('Location: ', geolocation.location)


#start our application
if __name__ == '__main__':
	main(ip_address)



"""
Python networking\allan>python geo_ip.py
GET IP Geolocation>> jkuat.ac.ke
[+]Domain IP translates to: 197.136.12.5
Country:  KE
Time zone:  Africa/Nairobi
Location:  (1.0, 38.0)
"""