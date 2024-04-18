from typing import List
from challenge3 import single_byte_xor_decipher


def detect_single_character_xor(hex_strs: List[str]):
    best_score = 0.0
    best_line = ""

    for hex_str in hex_strs:
        decrypted = single_byte_xor_decipher(hex_str)
        if decrypted[1] > best_score:
            best_line = decrypted[0]
            best_score = decrypted[1]
    return best_line


if __name__ == "__main__":
    num_lines: int = int(input())

    hex_strings = []
    for i in range(num_lines):
        hex_strings.append(input().strip())

    result = detect_single_character_xor(hex_strings)

    print(result)
