"""
Q: It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.

A: 142857
"""

from math import log10


def num_digits(n):
    return 1 + int(log10(n))


def digits_vector(n):
    # return a vector indicating digits present in n
    digits = [0] * 10
    while n:
        digits[n % 10] += 1
        n //= 10

    return digits


def permuted_multiples():
    # find smallest positive integer x s.t. x, 2x, ..., 6x,
    # contain the same digits.
    # 1) note 1x and 6x must have the same number of digits,
    #    which constrains how big is x.
    # 2) note also x must have at least 3 digits, otherwise
    #    by pigeonhole at least one pair from x, ..., 6x is
    #    the same number, which is a contradiction.
    x = 100
    while True:
        digit_vectors = [digits_vector(n * x) for n in range(2, 7)]
        if all(digits_vector(x) == dv for dv in digit_vectors):
            return x

        x += 1
        while num_digits(x) != num_digits(6 * x):
            x += 1


if __name__ == "__main__":
    print(
        "Smallest positive integer x such that "
        + "x, 2x, ..., 6x contain same digits: {}".format(permuted_multiples())
    )
