#!/usr/bin/python3
import nmap

def nmap_scan(ip_address, port):
    portscanner = nmap.PortScanner()  # Create an object from the library
    portscanner.scan(ip_address, port)  # Use scan function from the class

    # Ensure the IP exists in the scan result to avoid KeyError
    if ip_address in portscanner.all_hosts():
        # Save the state of the port
        state = portscanner[ip_address]['tcp'][int(port)]['state']

        print("[+] Executing command: ", portscanner.command_line())  # Fixed method name
        print(f"[+] {ip_address} tcp/{port} {state}")
    else:
        print(f"[-] No scan results for {ip_address}. Ensure the target is reachable.")

# Execute the main function
def main():
    # Get user input
    print("********" * 6)
    print("           Synchronous Scan ")
    print("********" * 6)
    
    ip_address = input("Enter the target IP>> ").strip()  # Strip to remove accidental spaces
    ports = input("Enter Ports to scan (comma-separated)>> ").strip().split(",")

    print("_______________________________________")

    for port in ports:
        port = port.strip()  # Remove extra spaces if the user entered "80, 443"
        if port.isdigit():  # Validate input is a number
            nmap_scan(ip_address, port)
        else:
            print(f"[-] Invalid port: {port}. Skipping...")

# Execute the program
if __name__ == "__main__":
    main()

'''
                                                                                
┌──(myenv)─(root㉿kali)-[/home/kali/python/scan_nmap]
└─# python synchronous_scan.py
************************************************
           Synchronous Scan 
************************************************
Enter the target IP>> 127.0.0.1
Enter Ports to scan (comma-separated)>> 21,22,80,5432
_______________________________________
[+] Executing command:  nmap -oX - -p 21 -sV 127.0.0.1
[+] 127.0.0.1 tcp/21 open
[+] Executing command:  nmap -oX - -p 22 -sV 127.0.0.1
[+] 127.0.0.1 tcp/22 open
[+] Executing command:  nmap -oX - -p 80 -sV 127.0.0.1
[+] 127.0.0.1 tcp/80 open
[+] Executing command:  nmap -oX - -p 5432 -sV 127.0.0.1
[+] 127.0.0.1 tcp/5432 open
'''
