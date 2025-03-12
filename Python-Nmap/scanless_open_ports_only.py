#!/usr/bin/python3
import scanless
import json

# Print a decorative header
print("********" * 6)
print("               Scanless Port Scanner")
print("********" * 6)

# Create an object from the class
s1 = scanless.Scanless()

# Get user input
target = input("Enter Target IP/Host name>> ").strip()
print("----------------------------------")
print("***** SCANNERS *****")
print("1. ipfingerprints")
print("2. spiderip")
print("3. standingtech")
print("4. viewdns")
print("5. yougetsignal")
option = int(input("Enter Service option: "))
print("---------------------------------------")

# Map user input to scanner name
scanner_options = {
    1: "ipfingerprints",
    2: "spiderip",
    3: "standingtech",
    4: "viewdns",
    5: "yougetsignal",
}
service = scanner_options.get(option)

# Validate scanner selection
if not service:
    print("Invalid option! Please choose a valid service (1-5).")
    exit(1)

# Execute the scan
output = s1.scan(target, scanner=service)

# Extract only open ports from the parsed output
if "parsed" in output and isinstance(output["parsed"], list):
    open_ports = []
    for port_info in output["parsed"]:
        if "state" in port_info and port_info["state"].lower() == "open":
            open_ports.append(f"Port {port_info['port']}: {port_info['service']}")

    if open_ports:
        print("\nOpen Ports:")
        print("\n".join(open_ports))
    else:
        print("No open ports found.")

else:
    print("Error: Could not retrieve scan results.")

# Print JSON output (optional for debugging)
# json_output = json.dumps(output, indent=2)
# print(json_output)



'''
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python open_scanless.py 
************************************************
               Scanless Port Scanner
************************************************
Enter Target IP/Host name>> scanme.nmap.org
----------------------------------
***** SCANNERS *****
1. ipfingerprints
2. spiderip
3. standingtech
4. viewdns
5. yougetsignal
Enter Service option: 5
---------------------------------------

Open Ports:
Port 22: ssh
Port 80: http
                     
'''