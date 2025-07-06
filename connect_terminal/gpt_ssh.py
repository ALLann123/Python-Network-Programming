#!/usr/bin/python3
import paramiko

ssh_client=paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh_client.connect(hostname='192.168.1.101', port=22, username='root', password='kali')


try:
    while True:
        command=input("SSH>> ")

        if command.lower() in ['exit', 'quit']:
            break

        stdin, stdout, stderr=ssh_client.exec_command(command)

        output=stdout.read().decode()

        error=stderr.read().decode()

        if output:
            print(output)

        if error:
            print(error)

finally:
    ssh_client.close()

