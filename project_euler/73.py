"""
Q: Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?

A: 7295372
"""

from math import gcd


def count_fractions(low, high, m):
    fractions = {}
    for d in range(2, m + 1):
        print(d)
        # restrict the search
        for n in range(int(d * low * (1 - 1.0 / (m / 10))), int(d * high) + 1):
            if gcd(n, d) == 1:
                s = str(n) + "/" + str(d)
                fractions[s] = 1.0 * n / d

    ordered_fractions = sorted(fractions, key=lambda k: fractions[k])

    # count fractions between low and high
    return len([f for f in ordered_fractions if low < fractions[f] < high])


if __name__ == "__main__":
    L, H, M = 1.0 / 3, 1.0 / 2, 12000
    print(
        "Number of reduced proper fractions between "
        + "{} and {} (d <= {}): {}".format(
            str(L), str(H), M, count_fractions(L, H, M)
        )
    )
