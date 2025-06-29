import codecs

def is_rot13(text):
    decoded = codecs.decode(text, 'rot_13')
    print(f"Original : {text}")
    print(f"ROT13 Decoded : {decoded}")
    return decoded

# Example usage:
encoded_string = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
# Extracting the part inside the curly braces
flag_body = encoded_string.split("{")[1].rstrip("}")
decoded_body = is_rot13(flag_body)
print(f"Decoded flag: picoCTF{{{decoded_body}}}")

"""
>python rot13_cryptography.py
Original : arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt
ROT13 Decoded : next_time_I'll_try_2_rounds_of_rot13_ulYvpVag
Decoded flag: picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}

"""