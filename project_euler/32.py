"""
Q: We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

A: 45228
"""

from math import log10


def pandigital(a, b, c):
    digits = [0] * 9
    while a:
        if a % 10 == 0:
            return False

        digits[a % 10 - 1] += 1
        a //= 10

    while b:
        if b % 10 == 0:
            return False

        digits[b % 10 - 1] += 1
        b //= 10

    while c:
        if c % 10 == 0:
            return False

        digits[c % 10 - 1] += 1
        c //= 10

    return digits == [1] * 9


def pandigitals_sum():
    seen = set()
    res = 0
    for i in range(1, 9999):
        for j in range(1, i):
            if (
                int(log10(i) + 1) + int(log10(j) + 1) + int(log10(i * j) + 1)
                > 9
            ):
                continue

            if pandigital(i, j, i * j) and not i * j in seen:
                print("pandigital: {}, {}, {}".format(i, j, i * j))
                seen.add(i * j)
                res += i * j

    return res


if __name__ == "__main__":
    print(
        "Sum of products with pandigital "
        "multiplicand/multiplier/product: {}".format(pandigitals_sum())
    )
