"""
Q: Euler discovered the remarkable quadratic formula:

  n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40*(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.

The incredible formula n^2 - 79*n + 1601 was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

  n^2 + a*n + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4.
Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.

A: -59231
"""

import math


def is_prime(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 2:
        return False

    m = int(math.sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def quadratic(n, a, b):
    return n ** 2 + a * n + b


def search():
    # O(N^2), search all possibilities
    # memoize primes to avoid recalculating
    memo = {}
    a_b_max_product = float("-inf")
    n_primes_max = float("-inf")
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(quadratic(n, a, b), memo):
                n += 1

            if n > n_primes_max:
                a_b_max_product = a * b
                n_primes_max = n

    return a_b_max_product


if __name__ == "__main__":
    print(
        "Product of coefficients a, b, for quadratic expression that produces"
        " the maximum number of primes for consecutive values of n: {}".format(
            search()
        )
    )
