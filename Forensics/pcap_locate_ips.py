#!/usr/bin/python3
from geoip import geolite2
import dpkt
import socket


def geolocation(ip_address):
    if ip_address.startswith("192.") or ip_address.startswith("10.") or ip_address.startswith("172."):
        return "Private IP"
    geolocation = geolite2.lookup(ip_address)
    if geolocation is not None:
        country = geolocation.country
        timezone = geolocation.timezone
        location = geolocation.location
        return f'{country}, {timezone}, {location}'
    return "Unknown"

def read_pcap(pcap_file):
	for ts, buf in pcap_file:
		try:
			eth=dpkt.ethernet.Ethernet(buf)
			ip=eth.data
			src=socket.inet_ntoa(ip.src)
			dst=socket.inet_ntoa(ip.dst)
			print(f"Source IP: {src}")
			print(f"Destination IP: {dst}")

			print(f'\n[+]Src: {geolocation(src)}--> Dst: {geolocation(dst)}')

		except Exception as e:
			print(f'Error Occured when reading pcap file: {e}')


if __name__=='__main__':
	pcap_file=input("PCAP file>> ")

	with open(pcap_file, 'rb') as file:
		pcap=dpkt.pcap.Reader(file)
		read_pcap(pcap)

"""
python pcap_locate_ips.py
PCAP file>> network.pcap
Source IP: 192.168.11.143
Destination IP: 192.168.11.128

[+]Src: None--> Dst: None
Source IP: 192.168.11.128
Destination IP: 192.168.11.143

[+]Src: None--> Dst: None
Source IP: 192.168.11.143
Destination IP: 192.168.11.128

[+]Src: None--> Dst: None
Source IP: 192.168.11.128
Destination IP: 192.168.11.143

[+]Src: None--> Dst: None
Source IP: 192.168.11.21
Destination IP: 128.115.14.97

[+]Src: None--> Dst: US, America/Los_Angeles, (37.6819, -121.768)
"""