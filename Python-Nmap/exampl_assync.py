#!/usr/bin/python3
import nmap
import time  # Import time for sleep

target = input("Enter the IP/Host name>> ")
print()

# Create a callback function
def nmap_callback(host, result):
    user = input("Shell>> ")
    print(f"User: {user}")
    print("---------------")
    print(result)

# Create an object from the class
a_scanner = nmap.PortScannerAsync()
output_scan=a_scanner.scan(target, arguments='-sS', callback=nmap_callback)  # FIXED: Use `target`

# Keep checking the scan status
while True:
    interact = input("Check the status/work on maths>> ")
    
    if "maths" in interact:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter Second number: "))
        print("Answer= ", num2 + num1)
   
    else:
        if not a_scanner.still_scanning():  # FIXED: Check scan completion
            break
    
    time.sleep(1)  # FIXED: Pause to allow scan progress
