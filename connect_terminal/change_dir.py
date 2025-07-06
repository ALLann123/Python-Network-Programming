#!/usr/bin/python3

import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='192.168.1.101', port=22, username='kali', password='kali')

current_dir = ""

try:
    while True:
        command = input("SSH>> ")
        if command.lower() in ['exit', 'quit']:
            break

        if command.startswith("cd "):
            # Update the current directory
            path = command[3:].strip()
            if path == "..":
                current_dir = "/".join(current_dir.rstrip("/").split("/")[:-1])
            elif path.startswith("/"):
                current_dir = path
            else:
                current_dir = f"{current_dir}/{path}".strip("/")

            continue  # Skip sending `cd` directly

        # Add current_dir to command using 'cd ... && actual_command'
        full_command = f"cd {current_dir} && {command}" if current_dir else command

        stdin, stdout, stderr = ssh_client.exec_command(full_command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(output)
        if error:
            print(error)

finally:
    ssh_client.close()


"""
SH>> pwd
/home/kali

SSH>> whoami
kali

SSH>> ls
"""