#!/usr/bin/python3
import socket
import struct

# Function to receive the file size from the client
def receive_file_size(sock: socket.socket):
    fmt = "<Q"  # Format for an unsigned long long (8 bytes)
    expected_bytes = struct.calcsize(fmt)  # Get the number of bytes required
    received_bytes = 0
    stream = bytes()  # Empty bytes object to store received data

    # Receive the file size in chunks until all bytes are received
    while received_bytes < expected_bytes:
        chunk = sock.recv(expected_bytes - received_bytes)  # Receive remaining bytes
        if not chunk:
            raise ConnectionError("Connection lost while receiving file size")
        stream += chunk
        received_bytes += len(chunk)

    filesize = struct.unpack(fmt, stream)[0]  # Unpack received bytes into an integer
    return filesize

# Function to receive a file from the client and save it
def receive_file(sock: socket.socket, filename):
    filesize = receive_file_size(sock)  # Get the file size
    with open(filename, "wb") as f:  # Open the file in binary write mode
        received_bytes = 0
        while received_bytes < filesize:
            chunk = sock.recv(1024)  # Receive file data in chunks of 1024 bytes
            if not chunk:
                break  # Exit loop if connection is lost
            f.write(chunk)  # Write received data to the file
            received_bytes += len(chunk)

# Create a server socket and listen for connections
with socket.create_server(("localhost", 9999)) as server:
    print("Waiting for client connection on localhost:9999...")

    # Accept a connection from the client
    connection, address = server.accept()
    with connection:  # Ensure connection closes properly when done
        print(f"[+] {address[0]}:{address[1]} connected")

        # Receive the filename from the client
        received_name = connection.recv(1024).decode()
        print(f"Receiving file: {received_name}...")

        # Receive and save the file
        receive_file(connection, received_name)
        print("[+] File Received!!")

'''
Running the program
Network>python receive_server.py
Waiting for client connection on localhost:9999...
[+] 127.0.0.1:64052 connected
Receiving file: hello.txt...
[+] File Received!!

J://code//python code//Mastering Python networking//Network>more hello.txt
Leave me Here!!
'''
