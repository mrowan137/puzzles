"""
Q: 2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

A: 232792560
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


def prime_factorization(n, primes):
    sz = len(primes)
    res = [0 for _ in range(sz)]
    for i in range(sz):
        while n % primes[i] == 0:
            res[i] += 1
            n /= primes[i]

    return res


def smallest_number_evenly_divided_by(i, j):
    # the final answer can be written in prime factorization as:
    #
    #   p0^a0 * p1^a1 * ... * pN^aN,
    #
    # where p0, ..., pN are successive primes.
    # the final product should be divisible by the numbers in the range [i, j],
    # each itself which can be written in prime factorization. the final answer
    # will be:
    #
    #   p0^max(a0_m) * p1^max(a1_m) * ... * pN^max(aN_m),
    #
    # where the max is taken over m numbers in the range [i, j].

    # calculational details:
    #   for each number in the range [i, j] we embed the prime factorization in
    #   a vector corresponding to primes up to j, e.g.
    #
    #     20 -->  [2, 0, 1, 0,  0,  0,  0,  0]
    #     primes: [2, 3, 5, 7, 11, 13, 17, 19]
    #
    #   this encoding makes it easy to loop over prime factorization for all
    #   numbers in the range [i, j].

    # compute prime numbers, up to the largest we need consider
    primes = []
    for n in range(2, j + 1):
        if is_prime(n):
            primes.append(n)

    number_to_prime_factorization = {}
    for n in range(i, j + 1):
        number_to_prime_factorization[n] = prime_factorization(n, primes)

    res = 1
    for i in range(len(primes)):
        p, exp = primes[i], float("-inf")
        for n in number_to_prime_factorization:
            exp = max(exp, number_to_prime_factorization[n][i])

        res *= p**exp

    return res


if __name__ == "__main__":
    i, j = 1, 20
    print(
        "Smallest positive number that is evenly "
        "divisible by all of the numbers from {} to {}: {}".format(
            i, j, smallest_number_evenly_divided_by(i, j)
        )
    )
