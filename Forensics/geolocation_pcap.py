#!/usr/bin/python3
import dpkt
import socket
import geoip2.database

def geolocation(ip_address):
	try:
		with geoip2.database.Reader('GeoLite2-City.mmdb') as gi:
			rec=gi.city(ip_address)
			city=rec.city.name
			country=rec.country.name
			continent=rec.continent.name
			latitude=rec.location.latitude
			longitude=rec.location.longitude
			return f'{city}, {country}, {continent}, {latitude}, {longitude}'

	except Exception as e:
		print(f'Error Occured: {e}')

def read_pcap(pcap_file):
	for ts, buf in pcap_file:
		try:
			eth=dpkt.ethernet.Ethernet(buf)
			ip=eth.data
			src=socket.inet_ntoa(ip.src)
			dst=socket.inet_ntoa(ip.dst)
			print(f'[+]Src: {geolocation(src)}--> Dst: {geolocation(dst)}')

		except Exception as e:
			print(f'Error Occured when reading pcap file: {e}')


if __name__=='__main__':
	pcap_file=input("PCAP file>> ")

	with open(pcap_file, 'rb') as file:
		pcap=dpkt.pcap.Reader(file)
		read_pcap(pcap)