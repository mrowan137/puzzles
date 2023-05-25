"""
Q: The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

  28 = 2^2 + 2^3 + 2^4
  33 = 3^2 + 2^3 + 2^4
  49 = 5^2 + 2^3 + 2^4
  47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?

A: 1097343
"""

from math import sqrt


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


def f(N, M_low, M_high, precomputed_primes, nums=[], s=0, seen=set()):
    # finds the number of prime sums S(p^b) <= N, where M_low, b <= M_high
    if M_low == M_high + 1:
        print("{}^2 + {}^3 + {}^4 = {}".format(nums[2], nums[1], nums[0], s))

        # make sure the sum was not seen previously
        res = s not in seen
        seen.add(s)
        return res

    # calculate up to p^M_high ~= N
    res = i = 0
    while i < len(precomputed_primes) and precomputed_primes[i] ** M_high <= N:
        nums.append(precomputed_primes[i])
        res += f(
            N - precomputed_primes[i] ** M_high,
            M_low,
            M_high - 1,
            precomputed_primes,
            nums,
            s + precomputed_primes[i] ** M_high,
            seen,
        )
        nums.pop(-1)
        i += 1

    return res


def answer(N, M_low, M_high):
    memo = {}
    primes = [x for x in range(2, int(sqrt(N)) + 1) if is_prime(x, memo)]
    print("Done calculating primes up to {}.".format(int(sqrt(N)) + 1))

    return f(N, M_low, M_high, primes)


if __name__ == "__main__":
    n = 50000000
    m_low = 2
    m_high = 4
    print(
        "Count of numbers below {} expressible as sum of ".format(n)
        + " primes quare, prime cube, and prime fourth power: {}".format(
            answer(n, m_low, m_high)
        )
    )
