import binascii

from oracle import *
import sys

if len(sys.argv) < 2:
    print("usage: python3 decipher.py <file>")
    sys.exit(-1)


def read_file(file_path):
    with open(file_path, 'r') as file:
        d = file.read()
    return d


def hex_to_list(hex_string):
    byte_data = binascii.unhexlify(hex_string)
    return [int(byte) for byte in byte_data]


def get_block(block_idx, ctext):
    return ctext[block_idx * 16:(block_idx + 1) * 16]


def put_block(block_data, block_idx, ctext):
    start = block_idx * 16
    end = (block_idx + 1) * 16
    ctext[start:end] = block_data[:16]


def get_pad_mask(pad_len, g, guessed):
    mask = [0] * 16

    if pad_len > 0:
        mask[16 - pad_len:] = [pad_len] * pad_len

    if guessed:
        mask[16 - len(guessed):] = [mask_val ^ guessed_val for mask_val, guessed_val in
                                    zip(mask[16 - len(guessed):], guessed)]

    if g:
        mask[16 - pad_len] ^= g

    return mask


def break_block(ctext, block_ind):
    guessed = []

    for pad_len in range(1, 16 + 1):
        for g in range(0, 256):
            if g == pad_len:
                continue

            copy = ctext[:]
            prev_block = get_block(block_ind - 1, copy)

            pad_mask = get_pad_mask(pad_len, g, guessed)
            prev_block = [x ^ p for x, p in zip(prev_block, pad_mask)]

            put_block(prev_block, block_ind - 1, copy)
            rc = Oracle_Send(copy[:(block_ind + 1) * 16], len(copy[:(block_ind + 1) * 16]) // 16)
            if rc == 1:
                guessed.insert(0, g)
                break

    return guessed


def pad_index(ctext):
    offset = len(ctext) - 2 * 16

    for i in range(16):
        copy = ctext[:]

        copy[offset + i] = 9
        rc = Oracle_Send(copy, len(copy) // 16)

        if rc == 1:
            copy[offset + i] = 30
            rc = Oracle_Send(copy, len(copy) // 16)

            if rc == 1:
                continue

        return i

    return -1


def break_last_block(ctext):
    ind = len(ctext) // 16 - 1
    pad_idx = pad_index(ctext[:])

    guessed = [16 - pad_idx] * (16 - pad_idx)

    for pad_len in range(16 - pad_idx + 1, 16 + 1, 1):
        for g in range(0, 256):
            copy = ctext[:]
            prev_block = get_block(ind - 1, copy)

            pad_mask = get_pad_mask(pad_len, g, guessed)
            prev_block = [x ^ p for x, p in zip(prev_block, pad_mask)]

            put_block(prev_block, ind - 1, copy)
            rc = Oracle_Send(copy, len(copy) // 16)
            if rc == 1:
                guessed.insert(0, g)
                break

    return guessed


data = read_file(sys.argv[1])
ctext_ls = hex_to_list(data)

Oracle_Connect()

guessed_bytes = [block for i in range(1, len(ctext_ls) // 16 - 1, 1) for block in break_block(ctext_ls, i)]
guessed_bytes += break_last_block(ctext_ls)

pad_length = guessed_bytes[-1]
del guessed_bytes[-pad_length:]

m_text = ''.join(chr(b) for b in guessed_bytes)
print(m_text)

recv = Oracle_Send(ctext_ls, len(ctext_ls) // 16)
print("received:", recv)

Oracle_Disconnect()
