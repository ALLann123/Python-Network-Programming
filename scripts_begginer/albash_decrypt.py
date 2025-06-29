#!/usr/bin/python3
# Define a function that performs Atbash cipher transformation
def atbash(text):
    result = ''  # This will store the transformed result

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet letter (ignores digits, symbols, etc.)
        if char.isalpha():
            if char.islower():
                # For lowercase letters: 'a' ↔ 'z', 'b' ↔ 'y', ..., 'm' ↔ 'n'
                # ord('a') = 97, ord('z') = 122 → 219 = 97 + 122
                result += chr(219 - ord(char))
            else:
                # For uppercase letters: 'A' ↔ 'Z', 'B' ↔ 'Y', ..., 'M' ↔ 'N'
                # ord('A') = 65, ord('Z') = 90 → 155 = 65 + 90
                result += chr(155 - ord(char))
        else:
            # If not a letter (like a digit or underscore), keep it unchanged
            result += char

    # Return the fully transformed string
    return result

# Example usage of the Atbash cipher function
ciphertext = "krxlXGU{zgyzhs_xizxp_xz00558y}"
plaintext = atbash(ciphertext)
print("Decrypted:", plaintext)

