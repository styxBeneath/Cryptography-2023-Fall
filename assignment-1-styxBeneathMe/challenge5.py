from codecs import *


def repeating_key_xor(key: str, text: str) -> str:
    key_length = len(key)
    text_bytes = text.encode("utf-8")

    encrypted = bytes(x ^ ord(key[i % key_length]) for i, x in enumerate(text_bytes))
    return encrypted.hex()


if __name__ == "__main__":
    input_key = input().strip()
    input_text = input().strip()

    result = repeating_key_xor(input_key, input_text)

    print(result)
