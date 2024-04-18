import base64


def hex_to_base64(hex_str: str) -> str:
    try:
        # hex string to binary data
        binary = bytes.fromhex(hex_str)

        # binary data to base64 string
        b64_str = base64.b64encode(binary).decode('utf-8')

        return b64_str
    except ValueError as ve:
        # invalid hex string
        return f"Error: {ve}"
    except Exception as e:
        # other exceptions
        return f"Unexpected error occurred: {e}"


if __name__ == "__main__":
    str_hex = input().strip()

    str_base64 = hex_to_base64(str_hex)

    print(str_base64)
