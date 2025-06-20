#!/usr/bin/python3
import requests

class IPGeolocation(object):
	def __init__(self, ip_address):
		self.latitude=''
		self.longitude=''
		self.country=''
		self.city=''
		self.time_zone=''
		self.ip_address=ip_address
		self.get_location()  #we call the fet location function

	def get_location(self):
		json_request=requests.get('http://ip-api.com/json/%s' % self.ip_address).json()

		print(json_request)
		if 'country' in json_request.keys():
			self.country=json_request['country']
		if 'countryCode' in json_request.keys():
			self.country_code=json_request['countryCode']
		if 'timezone' in json_request.keys():
			self.time_zone=json_request['timezone']
		if 'city' in json_request.keys():
			self.city=json_request['city']
		if 'lat' in json_request.keys():
			self.latitude=json_request['lat']
		if 'lon' in json_request.keys():
			self.longitude=json_request['lon']

#lets create an object from our class

if __name__ =='__main__':
	geolocation=IPGeolocation('102.219.208.125')
	print(geolocation.__dict__)


"""
                                                                          
┌──(root㉿kali)-[/home/kali/black_python]
└─# python ip_geolocation.py 
{'status': 'success', 'country': 'Kenya', 'countryCode': 'KE', 'region': '30', 'regionName': 'Nairobi County', 'city': 'Nairobi', 'zip': '09831', 'lat': -1.2841, 'lon': 36.8155, 'timezone': 'Africa/Nairobi', 'isp': 'Vijiji Connect Limited', 'org': '', 'as': 'AS328856 VIJIJI CONNECT LIMITED', 'query': '102.219.208.125'}
{'latitude': -1.2841, 'longitude': 36.8155, 'country': 'Kenya', 'city': 'Nairobi', 'time_zone': 'Africa/Nairobi', 'ip_address': '102.219.208.125', 'country_code': 'KE'}
                       
"""