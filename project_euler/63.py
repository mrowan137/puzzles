"""
Q: The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

A: 49
"""

from math import log10


def num_digits(n):
    return int(log10(n)) + 1


def powerful_digit_counts():
    # how much to check, what's the condition?
    #   log10(m^n) + 1 = n
    # there can be positive solutions to n for
    #   1 <= m <= 9
    # which gives us the range we need to check
    cnt = 0
    for m in range(1, 10):
        n = 1
        while True:
            nd = num_digits(m ** n)
            cnt += nd == n
            if nd == n:
                print("{}^{} = {} has {} digits".format(m, n, m ** n, nd))

            if nd <= n:
                if nd < n:
                    break

            n += 1

    return cnt


if __name__ == "__main__":
    print(
        "Number of n-digit positive integers which are also an nth power: "
        + "{}".format(powerful_digit_counts())
    )
