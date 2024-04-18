import os
from typing import Dict, Tuple

from util.frequencies import *


def calculate_score(decrypted_txt: str, frequencies_dict: Dict[str, float]):
    score = 0.0
    for letter in decrypted_txt:
        if letter.islower():
            score += frequencies_dict.get(letter, 0.0)

    return score


def single_byte_xor_decipher(encoded: str) -> tuple[str, float]:
    # obtain a dict of letter frequencies by parsing a text
    frequencies = get_letter_frequencies(os.path.join(os.path.dirname(__file__), 'util', 'kafka.txt')
                                         )

    best_score = 0.0
    best_line = ""

    try:
        # hex string to binary data
        hex_bytes = bytes.fromhex(encoded)

        for i in range(128):
            # XOR operation byte by byte
            original_bytes = bytes(x ^ i for x in hex_bytes)

            # binary data to string
            decrypted = original_bytes.decode('utf-8')
            current_score = calculate_score(decrypted, frequencies)

            # Update result if the current decryption has a higher score
            if current_score > best_score:
                best_score = current_score
                best_line = decrypted

        return best_line.strip(), best_score
    except ValueError as ex:
        return f"Invalid hex string: {ex}", 0
    except Exception as e:
        return f"Error: {e}", 0


if __name__ == "__main__":
    str_hex = input().strip()

    result = single_byte_xor_decipher(str_hex)[0]

    print(result)
