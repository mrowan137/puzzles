"""
Q: Euler's Totient function, φ(n) [sometimes called the phi function], is used
to determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of
79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.

A: 8319823
"""

from math import sqrt
from collections import Counter


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


def is_permutation(a, b):
    sa, sb = str(a), str(b)
    return Counter(sa) == Counter(sb)


def totient_permutation(m):
    # 1. number must be totient permutation
    # 2. n/phi(n) must be minimum
    # from first condition, observe n must be a non-prime,
    # because phi(p) = p - 1 will never be a permutation of p.
    # from second condition, we want phi(n) to be large
    # which can happen if n is coprime to many numbers.
    # so the next best scenario is n is a product of two primes.
    # Experiments with direct slow calculation, testing the guess
    # in a few cases:
    #   n = 10^2: 21    = 3*7
    #   n = 10^3: 291   = 3*97
    #   n = 10^4: 4435  = 5*887
    #   n = 10^5: 75841 = 149*509
    # ansatz: the number we seek is a product of two primes.
    # note phi(m*n) = phi(m)*phi(n) if m,n coprime.
    # so we could consider primes m, n, then phi(p) = p - 1
    # gives:
    #   phi(m*n) = (m - 1)*(n - 1)
    # and desired number will be from the set of:
    #   { m*n s.t. m*n = permutation( (m - 1)*(n - 1) ) }
    # save a factor of 3 in search range by noting min(m, n) >= 3.
    upper = int(m // 3) + 1
    memo, primes = {}, []
    for i in range(3, upper):
        if i % 1000 == 0:
            print("  i = {} / {}".format(i, upper - 1))
        if is_prime(i, memo):
            primes.append(i)

    print("Done calculating primes up to {}.".format(upper - 1))

    res, n_res = float("inf"), -1
    for i, pi in enumerate(primes):
        print("i = {} / {}".format(i, len(primes) - 1))
        for pj in primes[i:]:
            n = pi * pj
            if n <= m:
                euler_totient_n = (pi - 1) * (pj - 1)
                if is_permutation(n, euler_totient_n):
                    old_res = res
                    res = min(res, n / euler_totient_n)
                    if res < old_res:
                        n_res = n

    return n_res


if __name__ == "__main__":
    N = 10000000
    res = totient_permutation(N)
    print(
        "Value of n, 1 < n < {}, for which φ(n) is a permutation of n\n"
        "and ratio n/φ(n) produces a minimum: {}".format(N, res)
    )
