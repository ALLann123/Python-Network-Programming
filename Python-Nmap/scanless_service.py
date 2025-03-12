#!/usr/bin/python3
import scanless
import json
# Print a decorative header
print("********" * 6)
print("               Scanless Port Scanner")
print("********" * 6)

#create an object from the class
s1=scanless.Scanless()

#get user input
target=input("Enter Target IP/Host name>> ").strip()
print("----------------------------------")
print("*****SCANNERS*****")
print("1.ipfingerprints")
print("2.spiderip")
print("3.standingtech")
print("4.viewdns")
print("5.yougetsignal")
option=int(input("Enter Service option: "))
print("---------------------------------------")

service=''
if option == 1:
	service="ipfingerprints"
elif option == 2:
	service="spiderip"
elif option == 3:
	service="standingtech"
elif option == 4:
	service="viewdns"
elif option == 5:
	service="yougetsignal"

#use the object created to execute the scan function inthe class
output=s1.scan(target,scanner=service)

print(output['parsed'])
json_output= json.dumps(output, indent=2)
print(json_output)


'''
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python scanless_nmap.py 
************************************************
               Scanless Port Scanner
************************************************
Enter Target IP/Host name>> scanme.nmap.org
----------------------------------
*****SCANNERS*****
1.ipfingerprints
2.spiderip
3.standingtech
4.viewdns
5.yougetsignal
Enter Service option: 5
---------------------------------------
[{'port': '21', 'state': 'closed', 'service': 'ftp', 'protocol': 'tcp'}, {'port': '22', 'state': 'open', 'service': 'ssh', 'protocol': 'tcp'}, {'port': '23', 'state': 'closed', 'service': 'telnet', 'protocol': 'tcp'}, {'port': '25', 'state': 'closed', 'service': 'smtp', 'protocol': 'tcp'}, {'port': '53', 'state': 'closed', 'service': 'domain', 'protocol': 'tcp'}, {'port': '80', 'state': 'open', 'service': 'http', 'protocol': 'tcp'}, {'port': '110', 'state': 'closed', 'service': 'pop3', 'protocol': 'tcp'}, {'port': '115', 'state': 'closed', 'service': 'sftp', 'protocol': 'tcp'}, {'port': '135', 'state': 'closed', 'service': 'msrpc', 'protocol': 'tcp'}, {'port': '139', 'state': 'closed', 'service': 'netbios-ssn', 'protocol': 'tcp'}, {'port': '143', 'state': 'closed', 'service': 'imap', 'protocol': 'tcp'}, {'port': '194', 'state': 'closed', 'service': 'irc', 'protocol': 'tcp'}, {'port': '443', 'state': 'closed', 'service': 'https', 'protocol': 'tcp'}, {'port': '445', 'state': 'closed', 'service': 'microsoft-ds', 'protocol': 'tcp'}, {'port': '1433', 'state': 'closed', 'service': 'ms-sql-s', 'protocol': 'tcp'}, {'port': '3306', 'state': 'closed', 'service': 'mysql', 'protocol': 'tcp'}, {'port': '3389', 'state': 'closed', 'service': 'ms-wbt-server', 'protocol': 'tcp'}, {'port': '5632', 'state': 'closed', 'service': 'pcanywherestat', 'protocol': 'tcp'}, {'port': '5900', 'state': 'closed', 'service': 'vnc', 'protocol': 'tcp'}, {'port': '6112', 'state': 'closed', 'service': 'dtspc', 'protocol': 'tcp'}]
{
  "raw": "PORT      STATE  SERVICE\n21/tcp    closed ftp\n22/tcp    open   ssh\n23/tcp    closed telnet\n25/tcp    closed smtp\n53/tcp    closed domain\n80/tcp    open   http\n110/tcp   closed pop3\n115/tcp   closed sftp\n135/tcp   closed msrpc\n139/tcp   closed netbios-ssn\n143/tcp   closed imap\n194/tcp   closed irc\n443/tcp   closed https\n445/tcp   closed microsoft-ds\n1433/tcp  closed ms-sql-s\n3306/tcp  closed mysql\n3389/tcp  closed ms-wbt-server\n5632/tcp  closed pcanywherestat\n5900/tcp  closed vnc\n6112/tcp  closed dtspc",
  "parsed": [
    {
      "port": "21",
      "state": "closed",
      "service": "ftp",
      "protocol": "tcp"
    },
    {
      "port": "22",
      "state": "open",
      "service": "ssh",
      "protocol": "tcp"
    },
    {
      "port": "23",
      "state": "closed",
      "service": "telnet",
      "protocol": "tcp"
    },
    {
      "port": "25",
      "state": "closed",
      "service": "smtp",
      "protocol": "tcp"
    },
    {

'''