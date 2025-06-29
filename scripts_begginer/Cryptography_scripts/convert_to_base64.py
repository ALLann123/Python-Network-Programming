import base64

print("***********"*6)
print("       Convert To Base64  ")
print("***********"*6)
def main():
    user_input = input("Enter a string to encode in Base64: ").strip()

    encoded = base64.b64encode(user_input.encode()).decode()
    print("🔐 Base64 encoded string:", encoded)

if __name__ == "__main__":
    main()


"""
>python convert_to_base64.py
******************************************************************
       Convert To Base64
******************************************************************
Enter a string to encode in Base64: AllanMbugua
🔐 Base64 encoded string: QWxsYW5NYnVndWE=

>python id_base_64.py
Enter heck a string to cfor Base64: QWxsYW5NYnVndWE=
✅ Input is valid Base64.
🔓 Decoded content: AllanMbugua

"""