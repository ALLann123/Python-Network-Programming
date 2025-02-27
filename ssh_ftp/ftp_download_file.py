#!/usr/bin/python3
import ftplib  # Import the ftplib module for FTP operations

# Define the FTP server URL
ftp_server_url = 'ftp.be.debian.org'

# Define the directory path on the FTP server where the file is located
download_dir_path = 'www.kernel.org/pub/linux/kernel/v6.x/'

# Define the name of the file to be downloaded
download_file_name = 'ChangeLog-6.0'

def ftp_file_download(server, username):
    """
    Connects to the specified FTP server and downloads a file from the given directory.
    :param server: FTP server address
    :param username: Username for FTP authentication (anonymous login used here)
    """
    
    # Establish connection to the FTP server with the provided username
    ftp_client = ftplib.FTP(server, username)
    
    # Change the working directory to the specified download path on the FTP server
    ftp_client.cwd(download_dir_path)

    try:
        # Open a local file in write-binary mode to save the downloaded content
        with open(download_file_name, 'wb') as file_handler:
            # Construct the FTP command to retrieve the file
            ftp_cmd = 'RETR %s' % download_file_name
            
            # Retrieve the file in binary mode and write it to the local file
            ftp_client.retrbinary(ftp_cmd, file_handler.write)
            
            # Close the FTP connection
            ftp_client.quit()
    
    except Exception as exception:
        # Handle errors that may occur during the download process
        print('[-] File not downloaded: ', exception)

# Call the function to download the file using anonymous FTP login
ftp_file_download(server=ftp_server_url, username='anonymous')
