#!/usr/bin/python3
import urllib.request, json, sys, textwrap
import argparse

def cveSearch(cve):
	with urllib.request.urlopen('http://cve.circl.lu/api/cve/'+cve) as url:
		data=json.loads(url.read().decode())

		try:
			if data['cvss']:
				print("{} | CVSS {}".format(cve, data['cvss']))

			if data['summary']:
				print('+--Summary' + '-'*68+'\n')

				print('\n'.join(textwrap.wrap(data['summary'], 80)))
			if data['exploit-db']:
				print('+--ExploitDB' +'-'*66)
				for d in data['exploit-db']:
					print("| Title | {}". format(d['title']))
					print("| URL | {}".format(d['source']))

		except(TypeError, KeyError) as e:
			pass


print("[+]Search Exploit")
cve=input("Enter name>> ")
result=cveSearch(cve)
print(result)


