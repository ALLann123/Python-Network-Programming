import paramiko
import getpass

def ssh_client():
    print("****** SSH Client ******")
    
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
        print(f"Connected to {host}:{port} as {user}")
        
        while True:
            command = input("ssh> ")
            if command.lower() in ["exit", "quit"]:
                print("Closing SSH connection...")
                break
            
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if output:
                print(output)
            if error:
                print("Error:", error)
        
    except paramiko.AuthenticationException:
        print("Authentication failed! Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
        print("Disconnected.")

if __name__ == "__main__":
    ssh_client()





'''
                                                                                
┌──(kali㉿kali)-[~/python/ssh_ftp]
└─$ sudo python ssh_client.py
****** SSH Client ******
Enter IP/Hostname: 127.0.0.1
Enter Port (default 22): 22
Enter Username: kali
Enter Password: 
Connected to 127.0.0.1:22 as kali
ssh> whoami
kali

ssh> ls
Desktop
Documents
Downloads
John
Music
Pictures
Public
Templates

ssh> cd python
ssh> dir
Desktop    activate_python	     github
Documents  assembly_intel	     google-chrome-stable_current_amd64.deb
Downloads  automation		     list.txt
John	   black_python		     my_file.txt
Music	   chromedriver-linux64 
'''''