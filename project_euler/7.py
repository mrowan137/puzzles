"""
Q: By listing the first six prime numbers:

  2, 3, 5, 7, 11, and 13,

we can see that the 6th prime is 13. What is the 10001st prime number?

A: 104743
"""
from math import log


def at_least_first_n_primes(n):
    # use prime counting function approximation to guess
    # how big do we need to count; factor of 2 for safety
    # solve: x / log(x) >= 2*n
    x = 2
    while int(x / log(x)) < 2 * n:
        x += 1

    # cross off the non-prime numbers less than or equal to x
    # (i.e., the upper limit we calculated to count to get to n primes)
    numbers = list(range(2, x + 1))
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


def find_nth_prime(n):
    # numbers has crossed out multiples, anything that remains is prime
    numbers = at_least_first_n_primes(n)

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
