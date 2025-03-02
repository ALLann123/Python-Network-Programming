#!/usr/bin/python3
import paramiko

# Create an object
ssh_client = paramiko.SSHClient()

# Allow auto-accepting unknown host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Get user input
host = input("Enter the IP>> ")
name = input("Enter username: ")
pass_word = input("What is the password? ")

# Connect to the SSH server
try:
    ssh_client.connect(host, username=name, password=pass_word)
    print("Connected successfully!")
except paramiko.SSHException as e:
    print(f"SSH Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# Close the connection
ssh_client.close()
print("Bye!!")
