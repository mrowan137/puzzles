"""
Q: An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

A: 210
"""

from math import sqrt, log10


def num_digits(n):
    return 1 + int(log10(n))


def champernowne_nth_digit(n):
    # return nth digit of the fractional part;
    # i tracks which digit we reached, m is the number being appended
    i = 0
    m = 1
    while i < n:
        for j in range(num_digits(m)):
            i += 1
            if i == n:
                k = num_digits(m) - j - 1
                return (m // 10 ** k) % 10

        m += 1


if __name__ == "__main__":
    res = 1
    for i in range(7):
        res *= champernowne_nth_digit(10 ** i)

    print(
        "d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000: "
        + "{}".format(res)
    )
