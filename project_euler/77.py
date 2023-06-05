"""
Q: It is possible to write ten as the sum of primes in exactly five different
ways:
  7 + 3
  5 + 5
  5 + 3 + 2
  3 + 3 + 2 + 2
  2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?

A: 71
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


def prime_summations(target):
    # don't know a priori how big it needs to be, but we can print and check
    N = 100

    memo = {}
    primes = [x for x in range(2, N + 1) if is_prime(x, memo)]
    print(f"Done calculating primes up to {N + 1}.")

    # dp[i] is the number of prime summations yielding i
    dp = [1] + [0 for _ in range(N)]

    i = 0
    while i < len(primes):
        for j, _ in enumerate(dp):
            if j - primes[i] >= 0:
                dp[j] += dp[j - primes[i]]

        i += 1

    for i, v in enumerate(dp):
        print(f"{i} can be written as prime sums in {v} ways")

    i = 0
    while dp[i] < target:
        i += 1

    return i


if __name__ == "__main__":
    TARGET = 5000
    print(
        "First value that can be written as sum of primes in over"
        + f" {TARGET} ways: {prime_summations(TARGET)}"
    )
