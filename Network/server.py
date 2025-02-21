#!/usr/bin/python3
import socket

server_ip="127.0.0.1"
server_port=9999
#create a socket object
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#establish a connection to the port and ip for our socket
server.bind((server_ip,server_port))

#set server in listening mode.We provide number of connections to acccept
server.listen(10)  #10 clients can connect
print(f"[+]Server is listening on {server_ip}:{server_port} ")

#accept incoming connections
client, addr = server.accept()

#send data to the client
client.send("[+]I am Mr.Robot accepting connections on port 9999".encode())
print(f"[+]Accepted connection from: {addr}")

while True:
	#accepting data sent from the client
	request=client.recv(1024).decode()
	print(f"Receive message: {request}")

	if request != "quit":
		client.send(bytes("ACK", "utf-8"))
	else:
		break

client.close()
server.close()