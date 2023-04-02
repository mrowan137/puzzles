"""
Q: Euler's Totient function, phi(n) [sometimes called the phi function], is
defined as the number of positive integers not exceeding n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8 are all less than or equal to
nine and relatively prime to nine, phi(9) = 6.

n | Relatively Prime | phi(n) | n/phi(n)
2       1	        1	  2
3       1,2	        2	  1.5
4       1,3	        2	  2
5       1,2,3,4	        4	  1.25
6       1,5	        2	  3
7       1,2,3,4,5,6	6	  1.1666...
8       1,3,5,7	        4	  2
9       1,2,4,5,7,8	6	  1.5
10      1,3,7,9	        4	  2.5

It can be seen that n = 6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1000000 for which n/phi(n) is a maximum.

A: 510510
"""

from math import gcd


def coprimes(n):
    # return list of nums relatively prime to n
    return [i for i in range(1, n) if gcd(i, n) == 1]


def euler_totient(n):
    # return number of relative primes to n
    return len(coprimes(n))


def primes_less_than(n):
    # return primes less than n
    nums = list(range(2, n))

    for i in range(len(nums)):
        if nums[i] == -1:
            continue

        j = i
        while True:
            j += nums[i]

            if j >= len(nums):
                break

            nums[j] = -1

    return [m for m in nums if m != -1]


def totient_max(m):
    # find max of n/euler_totient(n), considering up to n <= m.
    # intuition: we want a big number that shares a lot of factors
    # with the numbers below it (this makes the numerator of n/phi(n)
    # big, and the denominator small). so we can take as trial
    # solutions, successive factors of primes

    # 1000 is definitely big enough
    primes = primes_less_than(100)

    i, n = 0, 1
    n_max, n_by_phi_max = -1, float("-inf")
    while True:
        n *= primes[i]
        i += 1

        if n >= m:
            break

        maybe_new_max = max(n_by_phi_max, 1.0 * n / euler_totient(n))
        if maybe_new_max > n_by_phi_max:
            n_max, n_by_phi_max = n, maybe_new_max

    return n_max, n_by_phi_max


if __name__ == "__main__":
    N = 1000000
    n_res, res = totient_max(N)
    print(
        "For 1 <= n <= {}, n/phi(n) reaches max for ".format(N)
        + "n = {} [ n/phi(n) = {} ]".format(n_res, res)
    )
