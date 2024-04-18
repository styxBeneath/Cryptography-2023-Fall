import os

from challenge1 import hex_to_base64
from challenge2 import fixed_xor
from challenge3 import single_byte_xor_decipher
from challenge4 import detect_single_character_xor
from challenge5 import repeating_key_xor


def test_challenge1():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests_1')

    i = 0
    while True:
        input_file = os.path.join(tests_dir, f'in_{i}.txt')
        output_file = os.path.join(tests_dir, f'out_{i}.txt')

        if not (os.path.exists(input_file) and os.path.exists(output_file)):
            break

        with open(input_file, 'r') as in_file, open(output_file, 'r') as out_file:
            for line_in, line_out in zip(in_file, out_file):
                hex_input = line_in.strip()
                expected_output = line_out.strip()

                result = hex_to_base64(hex_input)
                assert result == expected_output, f"Test failed for input '{hex_input}'"
                print(f"---------- assertion [{i + 1}] success ----------")

        i += 1


def test_challenge2():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests_2')

    i = 0
    while True:
        input_file = os.path.join(tests_dir, f'in_{i}.txt')
        output_file = os.path.join(tests_dir, f'out_{i}.txt')

        if not (os.path.exists(input_file) and os.path.exists(output_file)):
            break

        with open(input_file, 'r') as in_file, open(output_file, 'r') as out_file:
            for line1, line2 in zip(in_file, in_file):
                hex1 = line1.strip()
                hex2 = line2.strip()
                expected_output = out_file.readline().strip()

                result = fixed_xor(hex1, hex2)
                assert result == expected_output, f"Test failed for inputs '{hex1}' and '{hex2}'"
                print(f"---------- assertion [{i + 1}] success ----------")

        i += 1


def test_challenge3():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests_3')

    i = 0
    while True:
        input_file = os.path.join(tests_dir, f'in_{i}.txt')
        output_file = os.path.join(tests_dir, f'out_{i}.txt')

        if not (os.path.exists(input_file) and os.path.exists(output_file)):
            break

        with open(input_file, 'r') as in_file, open(output_file, 'r') as out_file:
            for line_in, line_out in zip(in_file, out_file):
                hex_input = line_in.strip()
                expected_output = line_out.strip()

                result = single_byte_xor_decipher(hex_input)[0]
                assert result == expected_output, f"Test failed for input {i}"
                print(f"---------- assertion [{i + 1}] success ----------")

        i += 1


def test_challenge4():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests_4')

    i = 0
    while True:
        input_file = os.path.join(tests_dir, f'in_{i}.txt')
        output_file = os.path.join(tests_dir, f'out_{i}.txt')

        if not (os.path.exists(input_file) and os.path.exists(output_file)):
            break

        with open(input_file, 'r') as in_file, open(output_file, 'r') as out_file:
            hex_strs = []
            for j, line_in in enumerate(in_file):
                if j == 0:
                    continue
                hex_strs.append(line_in.strip())

            expected_output = out_file.read().strip()

            result = detect_single_character_xor(hex_strs)
            assert result == expected_output, f"Test failed for input {i}"
            print(f"---------- assertion [{i + 1}] success ----------")

        i += 1


def test_challenge5():
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests_5')

    i = 0
    while True:
        input_file = os.path.join(tests_dir, f'in_{i}.txt')
        output_file = os.path.join(tests_dir, f'out_{i}.txt')

        if not (os.path.exists(input_file) and os.path.exists(output_file)):
            break

        with open(input_file, 'r') as in_file, open(output_file, 'r') as out_file:
            for j, line_in in enumerate(in_file):
                if j == 0:
                    input_key = line_in.strip()
                else:
                    input_text = line_in.strip()
            result = repeating_key_xor(input_key, input_text)

            expected_output = out_file.read().strip()
            assert result == expected_output, f"Test failed for input {i}"
            print(f"---------- assertion [{i + 1}] success ----------")

        i += 1


def test_challenge6():
    pass


if __name__ == "__main__":
    test_methods = [
        test_challenge1,
        test_challenge2,
        test_challenge3,
        test_challenge4,
        test_challenge5,
        test_challenge6,
    ]

    for test_num, test_method in enumerate(test_methods, start=1):
        print(f"Running test #{test_num}...")
        test_method()
        print(f"Test #{test_num} completed\n")

    print("All tests passed")
