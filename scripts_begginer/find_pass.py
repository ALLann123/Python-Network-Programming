import hashlib

# List of possible passwords from the challenge script
candidates = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

# Read the target hash from file
with open("level3.hash.bin", "rb") as f:
    target_hash = f.read()

# Try each candidate password
for password in candidates:
    # Calculate MD5 hash
    hashed = hashlib.md5(password.encode()).digest()

    # Compare with the hash in the file
    if hashed == target_hash:
        print(f"[+] Correct password found: {password}")
        break
else:
    print("[-] No matching password found.")


"""
python find_password.py 
[+] Correct password found: 87ab
                                                                             
┌──(root㉿kali)-[/home/kali/ctf_pico/python_ctf/ohh_crack_3]
└─# python level3.py       
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
                                  
"""



"""
More Hints:
1. Examine the Checker Script (level3.py):

It defines an MD5 hashing function for the input password.

It compares this with the binary level3.hash.bin.

If they match, it decrypts level3.flag.txt.enc using a simple XOR function (str_xor).

At the bottom, it also lists 7 candidate passwords:

python
Copy
Edit
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]


"""