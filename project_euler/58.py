"""
Q: Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

A: 26241
"""

from math import sqrt


def is_prime(n):
    if n < 2:
        return False

    m = int(sqrt(n))
    while m > 1:
        if n % m == 0:
            return False

        m -= 1

    return True


def spiral_primes(thresh):
    s = 1
    n_primes = 0
    n_diagonals = 1
    while 1.0 * n_primes / n_diagonals > thresh or s == 1:
        # add layers until falling below the threshold

        # side length increase by two
        s += 2

        # new layer adds 4 diagonals
        n_diagonals += 4

        # the new diagonals values can be deduced backwards
        # from the odd square at bottom right of the layer;
        # only the first 3 are potentially primes
        sm1 = s - 1
        diagonal_values = [s ** 2 - sm1, s ** 2 - 2 * sm1, s ** 2 - 3 * sm1]
        n_primes += sum(is_prime(dv) for dv in diagonal_values)

        print(
            "s = {}, n_primes/n_diagonals = {} ({}/{})".format(
                s, 1.0 * n_primes / n_diagonals, n_primes, n_diagonals
            )
        )

    return s


if __name__ == "__main__":
    thresh = 0.1
    print(
        "Side length for which ratio of primes along both diagonals "
        + "falls below {}: {}".format(thresh, spiral_primes(thresh))
    )
