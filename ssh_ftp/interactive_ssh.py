import paramiko
import getpass
import time
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
        
        # Open an interactive shell
        shell = client.invoke_shell()
        print(Fore.BLUE + "Interactive shell started. Use 'cd' to change directories." + Style.RESET_ALL)
        
        # Wait for the shell to initialize
        time.sleep(1)
        
        # Read the initial shell output (e.g., MOTD, login message)
        while shell.recv_ready():
            shell.recv(1024)
        
        # Set initial directory
        current_dir = "~"
        
        while True:
            # Prompt for command
            command = input(Fore.YELLOW + f"ssh:{current_dir}> " + Style.RESET_ALL).strip()
            
            if command.lower() in ["exit", "quit"]:
                print(Fore.RED + "Closing SSH connection..." + Style.RESET_ALL)
                break
            
            # Send the command to the shell
            shell.send(command + "\n")
            
            # Wait for the command to execute
            time.sleep(0.5)
            
            # Read the shell output
            output = ""
            while shell.recv_ready():
                output += shell.recv(1024).decode()
            
            # Clean up the output (remove the command echo and shell prompt)
            lines = output.splitlines()
            if lines:
                # Remove the command echo (first line)
                if lines[0].strip() == command:
                    lines.pop(0)
                # Remove the shell prompt (last line)
                if lines and lines[-1].strip().endswith("$"):
                    lines.pop(-1)
                # Join the remaining lines
                output = "\n".join(lines).strip()
            
            # Print the cleaned output
            if output:
                print(Fore.CYAN + output + Style.RESET_ALL)
            
            # Update the current directory for 'cd' commands
            if command.startswith("cd "):
                _, path = command.split(" ", 1)
                current_dir = path
        
    except paramiko.AuthenticationException:
        print(Fore.RED + "Authentication failed! Please check your credentials." + Style.RESET_ALL)
    except paramiko.SSHException as e:
        print(Fore.RED + f"SSH error: {e}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    finally:
        client.close()
        print(Fore.RED + "Disconnected." + Style.RESET_ALL)

if __name__ == "__main__":
    ssh_client()



'''
┌──(root㉿kali)-[/home/kali/python/ssh_ftp]
└─# python ssh_client.py
****** SSH Client ******
Enter IP/Hostname: 127.0.0.1
Enter Port (default 22): 22
Enter Username: kali
Enter Password: 
Connected to 127.0.0.1:22 as kali
Interactive shell started. Use 'cd' to change directories.
ssh:~> whoami
whoami

kali
                                                                                



kali@kali:~$ 
ssh:~> pwd
pwd

/home/kali
                                                                                



kali@kali:~$ 
ssh:~> ls
ls

Desktop    activate_python           github
Documents  assembly_intel            google-chrome-stable_current_amd64.deb
Downloads  automation                list.txt
John       black_python              my_file.txt
Music      chromedriver-linux64      open_list.py
Pictures   chromedriver-linux64.zip  python
Public     git_push_origin_master    shell_code
Templates  git_token                 tools
Videos     git_trojan
                                                                                



kali@kali:~$ 
ssh:~> cd python
cd python

                                                                                



kali@kali:~/python$ 
ssh:python> ls
ls

network  ssh_ftp  system_prog  traffic_sniffing
                                                                                



kali@kali:~/python$ 
ssh:python> exit
Closing SSH connection...
Disconnected.


'''