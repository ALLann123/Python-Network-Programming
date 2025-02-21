#!/usr/bin/python3

import argparse  # Using argparse instead of optparse
from socket import *
from threading import Thread

def socket_scan(host, port):
    """Attempts to connect to a given host and port, printing whether it is open or closed."""
    try:
        socket_connect = socket(AF_INET, SOCK_STREAM)
        socket_connect.settimeout(5)  # Set timeout for the connection attempt
        socket_connect.connect((host, port))
        print(f'[+] {port}/tcp OPEN')
    except Exception as error:
        print(f'[-] {port}/tcp CLOSED')
        print(f'[-] Reason: {str(error)}')
    finally:
        socket_connect.close()  # Ensure socket is closed after use

def port_scanning(host, ports):
    """Performs port scanning on the given host for the specified ports."""
    try:
        ip = gethostbyname(host)  # Resolve hostname to IP address
    except Exception as e:
        print(f"Unknown host: {host}. Error: {e}")
        return

    try:
        name = gethostbyaddr(ip)
        print(f"Scan Results for: {ip} ({name[0]})")
    except:
        print(f"Scan Results for: {ip}")

    for port in ports:
        t = Thread(target=socket_scan, args=(ip, int(port)))
        t.start()  # Start scanning each port in a new thread

def main():
    """Parses command-line arguments and initiates the port scanning process."""
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument('-H', '--host', type=str, required=True, help='Specify target host')
    parser.add_argument('-P', '--ports', type=str, required=True, help='Comma-separated list of ports')

    args = parser.parse_args()
    host = args.host
    ports = args.ports.split(',')  # Convert comma-separated ports into a list

    port_scanning(host, ports)

if __name__ == '__main__':
    main()


'''
The introduction of multithreading increased the port scanners speed
Running the progam
Network>python advanced_port_scanner.py -H scanme.nmap.org -P 22,23,80
Scan Results for: 45.33.32.156 (scanme.nmap.org)
[+] 80/tcp OPEN
[+] 22/tcp OPEN
[-] 23/tcp CLOSED
[-] Reason: timed out