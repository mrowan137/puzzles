"""
Q: A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

A: 4179871
"""

from math import sqrt

abundant = {}


def factors(n):
    res = set([1])
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)

    return res


def is_abundant(n):
    if n in abundant:
        return abundant[n]

    res = sum(factors(n)) > n

    abundant[n] = res
    return res


def non_twosum_abundant(n):
    for i in range(1, n // 2 + 1):
        if is_abundant(i) and is_abundant(n - i):
            return False

    return True


def sum_of_non_twosum_abundant_numbers():
    # analytical result that numbers greater than 28123
    # can be written as sum of two abundant numbers
    res = 0
    for i in range(1, 28123 + 1):
        if non_twosum_abundant(i):
            res += i

    return res


if __name__ == "__main__":
    print(
        "Sum of integers that can't be written "
        "as sum of two abundant numbers: {}".format(
            sum_of_non_twosum_abundant_numbers()
        )
    )
