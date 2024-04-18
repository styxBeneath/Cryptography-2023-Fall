import math


# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(p, g, h, max_x):
    block_size = 1 << 20
    base_pow_block = pow(g, block_size, p)
    base_inverse = pow(g, p - 2, p)
    hash_table = {}

    m = h
    for i in range(block_size):
        hash_table[m] = i
        m = (m * base_inverse) % p

    n = 1
    j = 0
    res = 0
    for j in range(block_size):
        if n in hash_table:
            res = hash_table[n]
            break
        n = (n * base_pow_block) % p

    return j * block_size + res


def main():
    # p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    # g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    # h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

    p = int(input().strip())
    g = int(input().strip())
    h = int(input().strip())
    max_x = 1 << 40  # 2^40

    dlog = discrete_log(p, g, h, max_x)
    print(dlog)


if __name__ == '__main__':
    main()
