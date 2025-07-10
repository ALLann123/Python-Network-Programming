#!/usr/bin/python3
import socket
import base64

#----Port identifier
#----base64
#----dns resolving

def port_identifier(num):
    user_pot=int(num)
    #get service name
    service_name=socket.getservbyport(user_pot, 'tcp')
    print(f"\nPort: {user_pot} => Service name: {service_name}")

def get_dns_record(target): # Returns the last IP found
    target
    ip=socket.gethostbyname(target)
    print(ip)

def convert_to_base64(text):
    encoded_text=base64.b64encode(text.encode()).decode()
    print(f"{text} to base64: {encoded_text}")

def convert_from_base64(text):
    decoded_text=base64.b64decode(text.encode()).decode()
    print(f"{text} \nfrom base64: {decoded_text}")


print("*****************"*6)
print("                         SCRIPTING   ")
print("*****************"*6)

while True:
    print("MY TOOL LIST ")
    print("1. Identify Port Service")
    print("2. Domain Name Resolution")
    print("3. Convert to Base64 ")
    print("4. Convert from Base64")

    user=input("\n pick a number(exit/quit)>> ")

    if user in ["exit", "quit"]:
        break

    if user == "1":
        num=input("Port Number: ")
        port_identifier(num)
    
    if user =="2":
        target=input("Enter domain: ")
        get_dns_record(target)

    if user =="3":
        text=input("Enter Text: ")
        convert_to_base64(text)

    if user =="4":
        text=input("Enter base64 text: ")
        convert_from_base64(text)

    print("---------------------------------------------------------------------------------------------------------------\n")




