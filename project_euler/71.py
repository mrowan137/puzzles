"""
Q: Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7,
  1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.

A: 428570
"""

from math import gcd


def ordered_fractions(m):
    fractions = {}
    for d in range(2, m + 1):
        print(d)
        # restrict the search
        for n in range(
            int(d * (3 * m / 10 - 1.0) / (7 * m / 10)), int(d * 3.0 / 7) + 1
        ):
            if gcd(n, d) == 1:
                s = str(n) + "/" + str(d)
                fractions[s] = 1.0 * n / d

    ordered_fractions = sorted(fractions, key=lambda k: fractions[k])

    # find 3/7
    i = 0
    while ordered_fractions[i + 1] != "3/7":
        i += 1

    return ordered_fractions[i]


if __name__ == "__main__":
    N = 1000000
    print("Fraction to the left of 3/7: {}".format(ordered_fractions(N)))
