"""
Q: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

A: 40730
"""

from math import factorial


def equals_to_sum_of_digit_factorials(n):
    res, n_orig = 0, n
    while n:
        if res > n_orig:
            return False

        res += factorial(n % 10)
        n //= 10

    return True if res == n_orig else False


def sum_digit_factorials():
    # consider constraint 9!*m == 10^m - 1
    # has the solution m~= 6.36; therefore
    # we need to consider numbers only up to
    # 6 digits long, because 9!*m < 10^m - 1
    # for m >= 7
    res = 0

    for n in range(3, 10 ** 6 - 1):
        if n % 1000 == 0:
            print(n)

        if equals_to_sum_of_digit_factorials(n):
            res += n

    return res


if __name__ == "__main__":
    print(
        "Sum of all numbers that equal sum of digit factorials: "
        "{}".format(sum_digit_factorials())
    )
