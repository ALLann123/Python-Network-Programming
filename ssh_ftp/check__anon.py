#!/usr/bin/python3
from ftplib import FTP, error_perm

def check_anonymous_login(hostname):
    try:
        # Create an FTP client object and connect to the server
        ftp_client = FTP(hostname)
        print(f"Connected to {hostname}")
        print("Server welcome message:", ftp_client.getwelcome())

        # Attempt to log in as anonymous
        print("Attempting anonymous login...")
        login_response = ftp_client.login()  # No username/password defaults to anonymous
        print("Login response:", login_response)

        # If login is successful, print a success message
        print("[+] Anonymous login is allowed on this server.")

        # Close the connection
        ftp_client.quit()
        print("Connection closed.")
        return True

    except error_perm as e:
        # Handle login errors
        print("[-] Anonymous login is NOT allowed on this server.")
        print("Error:", e)
        return False
    except Exception as e:
        # Handle other errors (e.g., connection issues)
        print("[-] An error occurred while connecting to the server.")
        print("Error:", e)
        return False

# Main function
def main():
    # Define the FTP server hostname
    hostname = 'ftp.be.debian.org'  # Replace with the target FTP server

    # Check if anonymous login is allowed
    print(f"Checking anonymous login for {hostname}...")
    if check_anonymous_login(hostname):
        print("Anonymous login check completed successfully.")
    else:
        print("Anonymous login check failed.")

# Entry point of the script
if __name__ == "__main__":
    main()

'''
python check__anon.py
Checking anonymous login for ftp.be.debian.org...
Connected to ftp.be.debian.org
Server welcome message: 220 ProFTPD Server (mirror.as35701.net) [::ffff:195.234.45.114]
Attempting anonymous login...
Login response: 230-Welcome to mirror.as35701.net.

 The server is located in Brussels, Belgium.

 Server connected with gigabit ethernet to the internet.

 The server maintains software archive accessible via ftp, http, https and rsync.

 ftp.be.debian.org is an alias for this host, but https will not work with that
 alias. If you want to use https use mirror.as35701.net.

 Contact: mirror-admin at as35701.net

230 Anonymous access granted, restrictions apply
[+] Anonymous login is allowed on this server.
Connection closed.
Anonymous login check completed successfully.
'''