#!/usr/bin/python3
import subprocess

print("*****"*6)
print("               NMAP SCRIPTING ENGINE PYTHON")
print("*****"*6)
target=input("Enter target IP/Host Name:")
p = subprocess.Popen(["nmap", "-sV", "--script", "vulners", target, "-p21,22,80"], strout=subprocess.PIPE)
(output,err) = p.communicate()
output = output.decode('utf-8').strip()

print(output)