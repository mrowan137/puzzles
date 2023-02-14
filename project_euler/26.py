"""
Q: A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

A: 983
"""

# Fraction with a prime denominator coprime to 10 produces a repeating decimal;
# length of the repeating part equals the order of 10 modulo p, i.e. the
# smallest positive integer k such that 10^k = 1 mod p.
# Strategy: for each prime p < 1000, compute the multiplicative order, and the
# one with largest multiplicative order has the longest repeating part.
# https://en.wikipedia.org/wiki/Repeating_decimal

import math


def multiplicative_order(a, n):
    # finds the smallest positive integer k such that
    # a^k = 1 mod n
    k = 1
    while (a ** k % n) != 1:
        k += 1

    return k


def is_prime(n):
    if n < 2:
        return False

    m = int(math.sqrt(n))
    while m > 1:
        if n % m == 0:
            return False

        m -= 1

    return True


def find_d_with_longest_cycle(n):
    d_max = -1
    max_cycle_length = float("-inf")

    for d in range(2, n):
        # check the primes, coprime to 10
        if is_prime(d) and d != 2 and d != 5:
            cycle_length = multiplicative_order(10, d)
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                d_max = d

    return d_max


if __name__ == "__main__":
    N = 1000
    print(
        "Value of d for which 1/d contains longest recurring cycle: {}".format(
            find_d_with_longest_cycle(N)
        )
    )
