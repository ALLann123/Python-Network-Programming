import base64

def is_base64(s):
    try:
        # Try decoding then encoding again to check if it matches
        decoded = base64.b64decode(s, validate=True)
        return base64.b64encode(decoded).decode().rstrip('=') == s.rstrip('=')
    except Exception:
        return False

def main():
    user_input = input("Enter a string to check for Base64: ").strip()

    if is_base64(user_input):
        decoded = base64.b64decode(user_input).decode(errors='ignore')
        print("✅ Input is valid Base64.")
        print("🔓 Decoded content:", decoded)
    else:
        print("❌ Input is NOT valid Base64.")

if __name__ == "__main__":
    main()


"""
python id_base_64.py
Enter a string to check for Base64: bDNhcm5fdGgzX3IwcDM1
✅ Input is valid Base64.
🔓 Decoded content: l3arn_th3_r0p35


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