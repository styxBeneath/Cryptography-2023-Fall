import binascii


def fixed_xor(hex1: str, hex2: str) -> str:
    try:
        # hex string to binary data
        binary1 = bytes.fromhex(hex1)
        binary2 = bytes.fromhex(hex2)

        if len(binary1) != len(binary2):
            raise ValueError("Hex strings must have the same length")

        # XOR operation byte by byte
        after_xor = bytes(x ^ y for x, y in zip(binary1, binary2))

        # binary data to hex string
        hex_result = binascii.hexlify(after_xor).decode('utf-8')

        return hex_result
    except ValueError as ve:
        # input length mismatch or other value-related errors
        return f"Error: {ve}"
    except Exception as e:
        # other exceptions
        return f"Unexpected error occurred: {e}"


if __name__ == "__main__":
    hex_1 = input().strip()
    hex_2 = input().strip()

    xor = fixed_xor(hex_1, hex_2)

    print(xor)
