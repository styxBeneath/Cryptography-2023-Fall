import math

from oracle import *
from helper import *


def get_signature(m, n):
    for div in range(2, math.isqrt(m) + 1):
        if m % div == 0:
            return (
                    Sign(div) *
                    Sign(m // div) *
                    pow(Sign(1), -1, n) % n
            )


def main():
    with open('project_3_2/input.txt', 'r') as f:
        n = int(f.readline().strip())
        msg = f.readline().strip()

    Oracle_Connect()

    m = ascii_to_int(msg)
    sigma = get_signature(m, n)

    print(sigma)

    Oracle_Disconnect()


if __name__ == '__main__':
    main()
