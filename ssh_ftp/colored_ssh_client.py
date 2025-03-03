import paramiko
import getpass
import os
from colorama import Fore, Style  # For colored output

def ssh_client():
    print(Fore.GREEN + "****** SSH Client ******" + Style.RESET_ALL)
    
    # Get connection details
    host = input("Enter IP/Hostname: ")
    port = int(input("Enter Port (default 22): ") or 22)
    user = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    
    try:
        # Initialize SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to SSH server
        client.connect(hostname=host, port=port, username=user, password=password)
        print(Fore.GREEN + f"Connected to {host}:{port} as {user}" + Style.RESET_ALL)
        
        # Initialize SFTP client
        sftp = client.open_sftp()
        print(Fore.BLUE + "SFTP session started. Use 'upload' or 'download' commands." + Style.RESET_ALL)
        
        while True:
            command = input(Fore.YELLOW + "ssh> " + Style.RESET_ALL).strip()
            if command.lower() in ["exit", "quit"]:
                print(Fore.RED + "Closing SSH connection..." + Style.RESET_ALL)
                break
            
            # Handle SFTP commands
            if command.startswith("upload"):
                _, local_path, remote_path = command.split()
                try:
                    sftp.put(local_path, remote_path)
                    print(Fore.GREEN + f"Uploaded {local_path} to {remote_path}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Upload failed: {e}" + Style.RESET_ALL)
                continue
            
            if command.startswith("download"):
                _, remote_path, local_path = command.split()
                try:
                    sftp.get(remote_path, local_path)
                    print(Fore.GREEN + f"Downloaded {remote_path} to {local_path}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Download failed: {e}" + Style.RESET_ALL)
                continue
            
            # Execute remote command
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if output:
                print(Fore.CYAN + output + Style.RESET_ALL)
            if error:
                print(Fore.RED + "Error: " + error + Style.RESET_ALL)
        
    except paramiko.AuthenticationException:
        print(Fore.RED + "Authentication failed! Please check your credentials." + Style.RESET_ALL)
    except paramiko.SSHException as e:
        print(Fore.RED + f"SSH error: {e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    finally:
        sftp.close()
        client.close()
        print(Fore.RED + "Disconnected." + Style.RESET_ALL)

if __name__ == "__main__":
    ssh_client()