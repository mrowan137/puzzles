"""
Q: Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 
  1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for
d ≤ 1,000,000?

A: 303963552391
"""

from math import gcd, sqrt


def is_prime(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = False
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            memo[n] = False
            return False

        m -= 1

    memo[n] = True
    return True


def primes_less_than(n, primes):
    i = 0
    while i < len(primes) and primes[i] < n:
        i += 1

    return primes[:i]


def euler_totient(n, precomputed_primes):
    primes = primes_less_than(n, precomputed_primes)
    res = n
    for p in primes:
        if n % p == 0:
            res *= 1 - 1.0 / p

    return res


def counting_fractions(m):
    # for given d, add one for each n<d when coprime(n, d);
    # prime p therefore adds p-1 new fractions;
    # non-prime adds phi(np), where phi is Euler Totient function and has
    # a convenient and easy to calculate known formula

    memo = {}
    primes = [n for n in range(2, m) if is_prime(n, memo)]
    print("Done calculating primes up to {}.".format(m))

    cnt = 0
    for d in range(2, m + 1):
        print("d = {}".format(d))
        if is_prime(d, memo):
            cnt += d - 1
        else:
            cnt += euler_totient(d, primes)

    return cnt


if __name__ == "__main__":
    M = 1000000
    print(
        "Number of reduced proper fractions n/d for d <= {}: {:d}".format(
            M, int(counting_fractions(M))
        )
    )
