import binascii

from oracle import *
import sys

if len(sys.argv) < 2:
    print("usage: python3 forge.py <file>")
    sys.exit(-1)


def read_file(file_path):
    with open(file_path, 'r') as file:
        d = file.read()
    return d


def split_into_blocks(ptext):
    blocks = [ptext[k:k + 16] for k in range(0, len(ptext), 16)]

    if len(blocks[-1]) < 16:
        blocks[-1] += [0] * (16 - len(blocks[-1]))

    if len(blocks) % 2 != 0:
        sys.exit(-1)

    return blocks


def xor(x, y):
    return list(map(lambda a, b: a ^ b, x, y))


def to_text(block):
    return ''.join(map(chr, block))


data = read_file(sys.argv[1])
p_text = list(map(ord, data))
blocks_ls = split_into_blocks(p_text)

Oracle_Connect()

t = Mac(to_text(blocks_ls[0] + blocks_ls[1]), 2 * 16)
for i in range(2, len(blocks_ls), 2):
    xored = xor(t, blocks_ls[i])
    text = to_text(xored + blocks_ls[i + 1])
    t = Mac(text, len(text))

res = Vrfy(data, len(data), t)

if res == 1:
    print(binascii.hexlify(t).decode('utf-8'))
else:
    print("verification failed.")

Oracle_Disconnect()
