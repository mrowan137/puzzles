"""
Q: The sum of the prime numbers below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all primes below two million.

A: 142913828922
"""
from math import log


def primes_below_n(n):
    # we can reuse from Problem 7;
    # cross off the non-prime numbers less than n
    numbers = list(range(2, n))
    for i in range(len(numbers)):
        if numbers[i] == -1:
            continue

        multiple_of_n = numbers[i]
        num = numbers[i]
        idx = i
        while idx + num < len(numbers):
            idx, multiple_of_n = idx + num, multiple_of_n + num
            numbers[idx] = -1

    return numbers


def sum_primes_below_n(n):
    # numbers has crossed out multiples, anything that remains is prime
    numbers = primes_below_n(n)

    i, cnt, res = 0, 0, 0
    while i < len(numbers):
        if numbers[i] != -1:
            res += numbers[i]

        i += 1

    return res


if __name__ == "__main__":
    n = 2000000
    res = sum_primes_below_n(n)
    print("Sum of primes below {}: {}".format(n, res))
