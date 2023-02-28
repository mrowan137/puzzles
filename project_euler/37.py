"""
Q: The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

A: 748317
"""

from math import sqrt, log10


def is_prime(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 2:
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def is_truncatable_prime(n):
    n_orig = n

    # right-to-left truncatable
    while n:
        if not is_prime(n):
            return False

        n //= 10

    # left-to-right truncatable
    n = n_orig
    while n:
        num_places = int(log10(n)) + 1
        if not is_prime(n):
            return False

        n %= 10 ** (num_places - 1)

    return True


def sum_truncatable_primes():
    # sum the only 11 truncatable primes (we are given there are only 11)
    res, cnt = 0, 0

    # start at 11, as 2, 3, 5, 7 are not considered truncatable primes
    n = 11
    while cnt < 11:
        if is_truncatable_prime(n):
            res += n
            cnt += 1

        n += 1

    return res


if __name__ == "__main__":
    print(
        "Sum of all 11 truncatable primes: {}".format(sum_truncatable_primes())
    )
