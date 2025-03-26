#!/usr/bin/python3  
from zapv2 import ZAPv2  
import sys  
import time  

apikey = ''  # Define the API key (should be set before running the script)
# Check if API key is provided
if apikey == '':
    print("API key not found!!")
    sys.exit()  # Exit the script if no API key is provided

# Print header for Spider Scan
print("*****" * 6)
print("         Spider Scan")
print("*****" * 6)

# Get the target URL from the user
target = input("Enter the target>> ")

# Initialize the ZAP API with the provided API key
zap = ZAPv2(apikey=apikey)

# Inform the user that spider scan is starting
print(f"[+] Spidering target {target}")

# Start the spider scan on the target and retrieve the scan ID
scanID = zap.spider.scan(target)

# Monitor the progress of the scan
while int(zap.spider.status(scanID)) < 100:
    print("Spider Progress %: {}".format(zap.spider.status(scanID)))
    time.sleep(1)  # Wait for 1 second before checking the status again

# Inform the user that the spider scan is complete
print('Spider has completed')

# Print the results of the spider scan
print('\n'.join(map(str, zap.spider.results(scanID))))

'''
──(myenv)─(root㉿kali)-[/home/kali/python/web_apps]
└─# python3 basic_spider.py
******************************
         Spider Scan
******************************
Enter the target>> http://testphp.vulnweb.com/
[+] Spidering target http://testphp.vulnweb.com/
Spider Progress %: 0
Spider Progress %: 0
Spider Progress %: 33
Spider Progress %: 12
Spider Progress %: 22
Spider Progress %: 25
Spider Progress %: 31
Spider Progress %: 34
Spider Progress %: 36
Spider Progress %: 36
Spider Progress %: 42
Spider Progress %: 55
Spider Progress %: 65
Spider Progress %: 71
Spider Progress %: 73
Spider Progress %: 76
Spider Progress %: 80
Spider Progress %: 91
Spider Progress %: 97
Spider Progress %: 98
Spider has completed
http://testphp.vulnweb.com/categories.php
http://testphp.vulnweb.com/showimage.php?file=./pictures/7.jpg
http://testphp.vulnweb.com/showimage.php?file=./pictures/6.jpg
http://testphp.vulnweb.com/signup.php
http://testphp.vulnweb.com/Flash/add.swf
http://testphp.vulnweb.com/showimage.php?file=./pictures/5.jpg
http://testphp.vulnweb.com/hpp/params.php?p=valid&pp=

'''
