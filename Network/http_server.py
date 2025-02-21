#!/usr/bin/python3
import socket

#create a socket object
mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#use the socket bind function 
mysocket.bind(('127.0.0.1', 8080))
#set the socket in listening mode
mysocket.listen(5)

while True:
	print("[+]Waiting for connections")
	((recv_socket, addr))=mysocket.accept()
	print(f"[+]HTTP request received: {addr}")
	print(recv_socket.recv(1024))
	recv_socket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n",'utf-8'))
	recv_socket.close()

'''
Using test_http_server.py to connect to the server we get
──(root㉿kali)-[/home/kali/python/network]
└─# python http_server.py  
[+]Waiting for connections
[+]HTTP request received: ('127.0.0.1', 38150)
b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
[+]Waiting for connections
'''
