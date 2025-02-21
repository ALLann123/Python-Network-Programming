#!/usr/bin/python3
import os
import socket
import struct

# Function to send a file to the server
def send_file(sock: socket.socket, filename):
    filesize = os.path.getsize(filename)  # Get the file size in bytes
    sock.sendall(struct.pack('<Q', filesize))  # Send the file size to the server

    with open(filename, "rb") as f:  # Open the file in binary read mode
        while (read_bytes := f.read(1024)):  # Read in chunks of 1024 bytes
            sock.sendall(read_bytes)  # Send the read bytes to the server

# Create a connection to the server
with socket.create_connection(("localhost", 9999)) as connection:
    print("Connecting to the server...")
    
    # Get the filename from the user
    file_to_send = input("Enter file name >> ")
    
    # Send the filename first so the server knows what file is being transferred
    connection.sendall(file_to_send.encode('utf-8'))
    
    print("Sending file...")
    
    # Call the function to send the file
    send_file(connection, file_to_send)
    
    print("[+] File sent!")

'''
Runing the code and providing file name
New folder>python send_file.py
Connecting to the server...
Enter file name >> hello.txt
Sending file...
[+] File sent!
'''