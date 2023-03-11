"""
Q: It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

A: 5777
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


def odd_composite(n, primes):
    # requires n <= max(primes)
    return n % 2 == 1 and not n in primes


def goldbachs_other_conjecture(n):
    # for n large enough, we can find the smallest
    # odd composite that cannot be written as the
    # sum of a prime and twice a square
    primes = primes_less_than(n)

    m = 9
    while m < n:
        if odd_composite(m, primes):
            i = 0
            while True:
                if i == len(primes) or primes[i] > m:
                    return m

                hopefully_square = (m - primes[i]) // 2
                if sqrt(hopefully_square) == int(sqrt(hopefully_square)):
                    print(
                        "{} = {} + 2*{}".format(m, primes[i], hopefully_square)
                    )
                    break

                i += 1

        m += 1

    print("Did not find counterexample, increase n!")
    return -1


if __name__ == "__main__":
    N = 100000
    print(
        "Smallest odd composite that cannot be written"
        + " as the sume of a prime and twice a square: {}".format(
            goldbachs_other_conjecture(N)
        )
    )
