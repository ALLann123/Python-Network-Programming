def detect_base(value: str) -> str:
    value = value.strip().lower()
    if value.startswith("0x"):
        return "hex"
    elif value.startswith("0b"):
        return "binary"
    elif all(c in "01" for c in value):
        return "binary"
    elif all(c in "0123456789abcdef" for c in value) and not any(c in "ghijklmnopqrstuvwxyz" for c in value):
        try:
            int(value, 10)
            return "decimal"
        except ValueError:
            return "hex"  # fallback for pure hex (without 0x)
    return "unknown"

def convert_number(value: str, source_format: str, target_format: str) -> str:
    # Convert input to int based on detected base
    if source_format == "hex":
        num = int(value, 16) if value.startswith("0x") else int(value, 16)
    elif source_format == "binary":
        num = int(value, 2) if value.startswith("0b") else int(value, 2)
    elif source_format == "decimal":
        num = int(value)
    else:
        raise ValueError("Unknown source format.")

    # Convert to target format
    if target_format == "decimal":
        return str(num)
    elif target_format == "hex":
        return hex(num)
    elif target_format == "binary":
        return bin(num)
    else:
        return "Unsupported target format."

def main():
    user_input = input("Enter a number (decimal, hex like 0x3D, or binary like 0b1101): ").strip()
    detected_format = detect_base(user_input)

    if detected_format == "unknown":
        print("❌ Unable to detect the format of the input.")
        return

    print(f"✅ Detected input format: {detected_format.upper()}")

    target_format = input("Convert to (decimal / hex / binary): ").strip().lower()
    try:
        result = convert_number(user_input, detected_format, target_format)
        print(f"🎯 Converted value: {result}")
    except Exception as e:
        print("❌ Error during conversion:", e)

if __name__ == "__main__":
    main()



"""
python convert_deci_hex_binary.py
Enter a number (decimal, hex like 0x3D, or binary like 0b1101): 0x3D
✅ Detected input format: HEX
Convert to (decimal / hex / binary): decimal
🎯 Converted value: 61

begginer>python convert_deci_hex_binary.py
Enter a number (decimal, hex like 0x3D, or binary like 0b1101): 0x3D
✅ Detected input format: HEX
Convert to (decimal / hex / binary): binary
🎯 Converted value: 0b111101

begginer>python convert_deci_hex_binary.py
Enter a number (decimal, hex like 0x3D, or binary like 0b1101): 0b111101
✅ Detected input format: BINARY
Convert to (decimal / hex / binary): decimal
🎯 Converted value: 61


>python convert_deci_hex_binary.py
Enter a number (decimal, hex like 0x3D, or binary like 0b1101): 42
✅ Detected input format: DECIMAL
Convert to (decimal / hex / binary): binary
🎯 Converted value: 0b101010

"""