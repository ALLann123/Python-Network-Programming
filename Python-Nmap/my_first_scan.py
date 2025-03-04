#!/usr/bin/python3
import nmap

#get input
print("------Python-NMAP-------------")
target=input("Enter host/IP>>")
port=input("Port Range>> ")
option_flag=input("Enter NMAP option to use>> ")
print("******************************************")
#create an object
port_scan=nmap.PortScanner()

results=port_scan.scan(target,port,option_flag)
print(results)


'''
                                                                             
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python my_first_scan.py  
------Python-NMAP-------------
Enter host/IP>>scanme.nmap.org
Port Range>> 22-80
Enter NMAP option to use>> -sS
******************************************
{'nmap': {'command_line': 'nmap -oX - -p 22-80 -sS scanme.nmap.org', 'scaninfo': {'tcp': {'method': 'syn', 'services': '22-80'}}, 'scanstats': {'timestr': 'Tue Mar  4 22:20:25 2025', 'elapsed': '4.98', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'45.33.32.156': {'hostnames': [{'name': 'scanme.nmap.org', 'type': 'user'}, {'name': 'scanme.nmap.org', 'type': 'PTR'}], 'addresses': {'ipv4': '45.33.32.156'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'reset'}, 'tcp': {22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}}
                                                   
'''