#!/usr/bin/python3 
from zapv2 import ZAPv2  
import time 

api_key = ''  # Define API key for ZAP (leave blank if not needed)
# Get the target URL from the user
target = input("Enter the target>> ")
print("------------------------------")
# Initialize the ZAP API client
zap = ZAPv2(apikey=api_key)
print(f"Accessing target {target}")

# Open the target URL in ZAP
zap.urlopen(target)
time.sleep(2)  # Wait for 2 seconds to ensure the request is processed

print()
print(f"Active Scanning target {target}")

# Start an active scan on the target and retrieve the scan ID
scanID = zap.ascan.scan(target)

# Monitor the scan progress until it reaches 100%
while int(zap.ascan.status(scanID)) < 100:
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)  # Wait for 5 seconds before checking again
print('Active scan completed')
print("====================================")
# Generate and save the scan report in HTML format
with open("report.html", "w") as report_file:
    report_file.write(zap.core.htmlreport())


'''
─(myenv)─(root㉿kali)-[/home/kali/python/web_apps]
└─# python3 active_scan.py    
Enter the target>> http://testphp.vulnweb.com/
------------------------------
Accessing target http://testphp.vulnweb.com/

Active Scanning target http://testphp.vulnweb.com/
Scan progress %: 0
Scan progress %: 7
Scan progress %: 14
Scan progress %: 31
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 39
Scan progress %: 42
Scan progress %: 53
Scan progress %: 58
Scan progress %: 58
Scan progress %: 58
Scan progress %: 58
Scan progress %: 70
Scan progress %: 83
Scan progress %: 86
Scan progress %: 86
Scan progress %: 86
Scan progress %: 92
Scan progress %: 92
Scan progress %: 95
Active scan completed
====================================
'''