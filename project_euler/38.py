"""
Q: Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

A: 932718654
"""

from math import log10


def num_digits(n):
    # count of digits in n
    return int(log10(n)) + 1


def pad(n, d):
    # pad n with d zeros on the right
    if n == 0:
        return 0

    return n * 10 ** d


def product(x, y):
    res = 0
    for y_i in y:
        partial_product = x * y_i
        d = num_digits(partial_product)
        res = pad(res, d)
        res += partial_product

    return res


def is_pandigital(n):
    # does the number contain all digits 1 -- 9?
    digits = [0] * 9
    while n:
        if n % 10 == 0:
            return False

        digits[n % 10 - 1] += 1
        n //= 10

    return digits == [1] * 9


def largest_pandigital():
    # compute product of x, y,
    # iterating x until product would be too many digits,
    # then reset x and iterating over y = [1], [1, 2], ..., [1, ..., 9]
    y = [1]
    res = float("-inf")
    for i in range(2, 10):
        y += [i]
        x = 1
        while True:
            p = product(x, y)
            if num_digits(p) > 9:
                break

            if is_pandigital(p):
                res = max(res, p)

            x += 1

    return res


if __name__ == "__main__":
    print(
        "Largest pandigital formed as the concatenated product of integer "
        "with (1,2, ... , n) where n > 1: {}".format(largest_pandigital())
    )
