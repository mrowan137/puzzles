"""
Q: The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

A: 55
"""


from math import log10, sqrt


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


def is_circular_prime(n, primes, memo={}):
    # expects n <= max(primes)
    if n in memo:
        return memo[n]

    n_orig = n
    rotations = [n]
    while True:
        # prime check
        if not n in primes:
            for r in rotations:
                memo[r] = False

            return False

        # cycle digits
        ones_digit = n % 10
        number_of_digits = int(log10(n)) + 1
        n //= 10
        n += ones_digit * 10 ** (number_of_digits - 1)
        rotations.append(n)

        # wrap check
        if n == n_orig:
            for r in rotations:
                memo[r] = True

            return True


def count_circular_primes(n):
    primes = primes_less_than(n)

    cnt, memo = 0, {}
    for p in primes:
        print(p)
        if is_circular_prime(p, primes, memo):
            cnt += 1

    return cnt


if __name__ == "__main__":
    N = 1000000
    print(
        "Count of circular primes below {}: "
        "{}".format(N, count_circular_primes(N))
    )
