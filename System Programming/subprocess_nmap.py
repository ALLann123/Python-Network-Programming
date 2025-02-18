#!/usr/bin/python3
from subprocess import Popen, PIPE

target=input("Enter target ip>> ")
process=Popen(['nmap', target], stdout=PIPE, stderr=PIPE)
stdout,stderr=process.communicate()    #waits for the process to finish
print(stdout.decode())

