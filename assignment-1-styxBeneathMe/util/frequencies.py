# data from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
default_frequencies = {
    'e': 11.1607,
    'a': 8.4966,
    'r': 7.5809,
    'i': 7.5448,
    'o': 7.1635,
    't': 6.9509,
    'n': 6.6544,
    's': 5.7351,
    'l': 5.4893,
    'c': 4.5388,
    'u': 3.6308,
    'd': 3.3844,
    'p': 3.1671,
    'm': 3.0129,
    'h': 3.0034,
    'g': 2.4705,
    'b': 2.0720,
    'f': 1.8121,
    'y': 1.7779,
    'w': 1.2899,
    'k': 1.1016,
    'v': 1.0074,
    'x': 0.2902,
    'z': 0.2722,
    'j': 0.1965,
    'q': 0.1962
}


def get_letter_frequencies(file_path):
    letter_frequencies = {}
    total_letters = 0.0

    try:
        with open(file_path, 'r') as file:
            content = file.read()

            for char in content:
                if char.islower():
                    letter_frequencies[char] = letter_frequencies.get(char, 0) + 1.0
                    total_letters += 1

            for letter in letter_frequencies:
                letter_frequencies[letter] /= total_letters / 100  # percentage

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return default_frequencies
    except Exception as e:
        print(f"An error occurred: {e}")
        return default_frequencies

    return letter_frequencies
