#!/usr/bin/python3
import socket

#create a socket object
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #using IPv4 and TCP connection

#connect to the target
sock.connect(('ftp.debian.org', 80))

#request a document. In our command we are sending a http get request to the server
cmd='GET http://ftp.debian.org/debian/README.mirrors.txt HTTP/1.0\r\n\r\n'.encode()

#used for sending bytes of data to the specified target
sock.send(cmd)

while True:
	#we receive the data requested from the buffer
	data=sock.recv(512)
	if len(data)<1:  #these terminates the program when there is no data being received and is less than one
		break
	print(data.decode(), end='')

sock.close()

'''
Lets run the program
shell>> python socket_web_server.py
HTTP/1.1 200 OK
Connection: close
Content-Length: 86
Server: Apache
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
Referrer-Policy: no-referrer
X-Xss-Protection: 1
Permissions-Policy: interest-cohort=()
Last-Modified: Sat, 04 Mar 2017 20:08:51 GMT
ETag: "56-549ed3b25abfb"
X-Clacks-Overhead: GNU Terry Pratchett
Content-Type: text/plain; charset=utf-8
Via: 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Age: 0
Date: Tue, 18 Feb 2025 16:22:38 GMT
X-Served-By: cache-ams2100134-AMS, cache-cpt13820-CPT
X-Cache: HIT, MISS
X-Cache-Hits: 140, 0
X-Timer: S1739895758.348014,VS0,VE151
Vary: Accept-Encoding

The list of Debian mirror sites is available here: https://www.debian.org/mirror/list'''

