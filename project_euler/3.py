"""
Q: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

A: 6857
"""

import math


def is_prime(n, memo={}):
    if n < 2:
        return False

    if n in memo:
        return memo[n]

    m = int(math.sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def largest_prime_factor(n):
    # search upward from 2 to make best use of memo,
    # and check if the other factor is prime
    m = 2
    memo = {}
    while m < n:
        if n % m == 0:
            other_factor = n // m
            if is_prime(other_factor, memo):
                return other_factor
        m += 1

    # we'll get here if n is prime
    return n


if __name__ == "__main__":
    n = 600851475143
    print(
        "Largest prime factor of n = {}: {}".format(n, largest_prime_factor(n))
    )
