import hashlib

# Load the target hash to compare against
with open("level5.hash.bin", "rb") as f:
    target_hash = f.read()

# Open the wordlist and loop through each word
with open("dictionary.txt", "r") as wordlist:
    for line in wordlist:
        password = line.strip()  # Remove newline characters
        hashed = hashlib.md5(password.encode()).digest()

        if hashed == target_hash:
            print(f"[+] Password found: {password}")
            break
    else:
        print("[-] No password match found.")
