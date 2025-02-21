#!/usr/bin/python3
import socket

webhost='localhost'
webport=8080

print(f'[+]Contacting: {webhost} on port:{webport}')
webclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

webclient.connect((webhost,webport))
webclient.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n".encode('utf-8')))

reply=webclient.recv(4096)

print(f"Response from: {webhost}")
print(reply.decode())


'''
Connecting to the web server. Status code 200 means we are able to connect
┌──(root㉿kali)-[/home/kali/python/network]
└─# python test_http_server.py
[+]Contacting: localhost on port:8080
Response from: localhost
HTTP/1.1 200 OK

 <html><body><h1>Hello World!</h1></body></html> 

