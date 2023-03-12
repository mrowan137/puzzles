"""
Q: The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?

A: 134043
"""


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


def prime_factorization(n, primes):
    sz = len(primes)
    res = [0 for _ in range(sz)]
    for i in range(sz):
        if n == 1:
            break

        while n % primes[i] == 0:
            res[i] += 1
            n /= primes[i]

    return res


def distinct_prime_factors(k, m):
    # find first k consecutive numbers to have k distinct prime factors,
    # checking up to max number m
    primes = primes_less_than(m + 1)

    number_to_prime_factorization = {}
    for n in range(2, m + 1):
        print("computing prime factorization: {}".format(n))
        number_to_prime_factorization[n] = prime_factorization(n, primes)

    cnt = 0
    for n in number_to_prime_factorization:
        print("check for distinct primes: {}".format(n))
        if cnt == k:
            return n - k
        if sum(bool(p) for p in number_to_prime_factorization[n]) == k:
            cnt += 1
        else:
            cnt = 0

    print(
        "Did not find {} consecutive numbers".format(k)
        + " with {} distinct prime factors. Increase search range!".format(k)
    )
    return -1


if __name__ == "__main__":
    K, M = 4, 200000
    ans = distinct_prime_factors(K, M)
    print(
        "The nums {} -- {} each have {} distinct prime factors.".format(
            ans, ans + K - 1, K
        )
    )
