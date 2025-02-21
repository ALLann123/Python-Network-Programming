#!/usr/bin/python3
import socket

host="127.0.0.1"
port=9999
try:
	#create socket object
	socket_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#connect to the target server
	socket_client.connect((host,port))
	print(f"Connected to server: {host} on port: {port}")
	#accept message from the server
	message=socket_client.recv(1024)

	print("[+]message received>> ", message.decode())
	while True:
		#send message  to the server
		message=input("Enter your message>>")
		socket_client.sendall(bytes(message.encode('utf-8')))
		if message=="quit":
			break
except socket.errno as error:
	print("Socket error", error)
finally:
	socket_client.close()