#!/usr/bin/python3
from ftplib import FTP

# Connect to the FTP server
ftp_client = FTP('ftp.be.debian.org')

# Get and print the welcome message
print("Server:", ftp_client.getwelcome())

# Log in to the FTP server (anonymous login)
print(ftp_client.login())

print("[+] Files and directories in the root directory:")
ftp_client.dir()

# Change to the correct directory
ftp_client.cwd('/www.kernel.org/')
print("[+] Changed to /www.kernel.org/ directory.")

# List files in the directory
files = ftp_client.nlst()
files.sort()

print()
print(f"{len(files)} files in /www.kernel.org/ directory:")

for file in files:
    print(file)

# Close the connection
ftp_client.quit()



'''
python ftp_listing_files.py
Server: 220 ProFTPD Server (mirror.as35701.net) [::ffff:195.234.45.114]
230-Welcome to mirror.as35701.net.

 The server is located in Brussels, Belgium.

 Server connected with gigabit ethernet to the internet.

 The server maintains software archive accessible via ftp, http, https and rsync.

 ftp.be.debian.org is an alias for this host, but https will not work with that
 alias. If you want to use https use mirror.as35701.net.

 Contact: mirror-admin at as35701.net

230 Anonymous access granted, restrictions apply
[+] Files and directories in the root directory:
drwxr-xr-x   9 ftp      ftp          4096 Feb 28 15:26 debian
drwxr-xr-x   5 ftp      ftp           105 Jan 12 05:27 debian-cd
drwxr-xr-x   7 ftp      ftp          4096 Feb 27 22:32 debian-security
drwxr-xr-x   5 ftp      ftp          4096 Oct 13  2006 ftp.irc.org
-rw-r--r--   1 ftp      ftp           432 Jul  9  2021 HEADER.html
drwxr-xr-x   5 ftp      ftp          4096 Feb 28 12:59 mint
drwxr-xr-x   5 ftp      ftp            49 Nov 30  2015 mint-iso
lrwxrwxrwx   1 ftp      ftp            33 Apr 29  2021 pub -> /var/www/html/www.kernel.org/pub/
drwxr-xr-x   7 ftp      ftp          4096 Feb 28 13:51 ubuntu
drwxr-xr-x  38 ftp      ftp          4096 Feb 28 13:46 ubuntu-cdimage
drwxr-xr-x  30 ftp      ftp          4096 Feb 28 09:22 ubuntu-cloudimages
drwxr-xr-x   7 ftp      ftp          4096 Feb 28 14:30 ubuntu-ports
drwxr-xr-x  15 ftp      ftp          4096 Feb 28 10:16 ubuntu-releases
drwxr-xr-x  25 ftp      ftp           303 Feb 28 08:04 video.fosdem.org
-rw-r--r--   1 ftp      ftp           390 Jul  9  2021 welcome.msg
drwxr-xr-x   4 ftp      ftp          4096 Jun 14  2023 www.kernel.org
[+] Changed to /www.kernel.org/ directory.

2 files in /www.kernel.org/ directory:
lost+found
pub'''
