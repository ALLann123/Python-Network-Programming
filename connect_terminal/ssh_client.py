#!/usr/bin/python3

import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



while True:
    ssh_client.connect(hostname='192.168.1.101', port=22, username='kali', password='kali')
    user=input("User>> ")
    print("-------------------------------------------------------------------------")
    if user.lower()=="exit":
        break
    else:
        stdin, stdout, stderr = ssh_client.exec_command(user)

        print(stdout.readlines())
        print(stderr.readlines())
        print()
