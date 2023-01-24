"""
Q: By listing the first six prime numbers:

  2, 3, 5, 7, 11, and 13,

we can see that the 6th prime is 13. What is the 10 001st prime number?

A: 104743
"""
from math import log


def primes_less_than(m):
    # use prime counting function approximation to guess
    # how big do we need to count; factor of 2 for safety
    # Solve: x / log(x) >= 2*m
    x = 2
    while int(x / log(x)) < 2 * m:
        x += 1

    # cross off the non prime numbers less than or equal to n
    numbers = list(range(2, x + 1))
    for i in range(len(numbers)):
        if numbers[i] == -1:
            continue

        multiple_of_n = numbers[i]
        n = numbers[i]
        idx = i
        while idx + n < len(numbers):
            idx, multiple_of_n = idx + n, multiple_of_n + n
            numbers[idx] = -1

    return numbers


def find_nth_prime(n):
    # numbers has crossed out multiples, anything that remains is prime
    numbers = primes_less_than(n)

    i, cnt = 0, 0
    while i < len(numbers):
        if numbers[i] != -1:
            cnt += 1
            if cnt == n:
                return numbers[i]

        i += 1

    return -1


if __name__ == "__main__":
    n = 10001
    nth_prime = find_nth_prime(n)
    print("{}th prime number: {}".format(n, nth_prime))
