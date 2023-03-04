"""
Q: We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

A: 7652413
"""

from math import log10, sqrt


def num_digits(n):
    # number of digits in n
    return 1 + int(log10(n))


def pad(n, d):
    # pad n with d zeros on the right
    if n == 0:
        return 0

    return n * 10 ** d


def pandigitals(n):
    # generate all n-digit pandigitals
    if n == 1:
        return [1]

    res = []
    for p in pandigitals(n - 1):
        # for each (n - 1)-digit pandigital, construct the n-digit
        # by inserting n in all possible locations

        d = num_digits(p)
        for i in range(d + 1):
            left = pad(p // (10 ** (d - i)), d - i + 1)
            mid = n * 10 ** (d - i)
            right = p % (10 ** (d - i))
            new_pandigital = left + mid + right
            res.append(new_pandigital)

    return res


def is_prime(n):
    # no memoization needed, since we will only inspect counting
    # down from the largest pandigital required (and so will only
    # see each inspected number once)
    if n < 2:
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            return False

        m -= 1

    return True


def largest_pandigital_prime():
    # count down from largest pandigital we need to consider.
    # we can observe sum(1 .. 9) = 9*10/2 = 45 which is divisible
    # by 3, thus there is no 9-digit pandigital prime (as it is divisible
    # by 3). similarly, sum(1 .. 8) = 8*9/2 = 36 which is divisible by 3,
    # thus 8-digit pandigital numbers are also divisible by 3.
    # with this information we can save some work to start inspection
    # from 7-digit pandigitals.
    for i in range(7, 0, -1):
        sorted_pandigitals = sorted(pandigitals(i), key=lambda x: -x)
        for p in sorted_pandigitals:
            if is_prime(p):
                return p


if __name__ == "__main__":
    print("Largest pandigital prime: {}".format(largest_pandigital_prime()))
