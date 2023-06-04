"""
Q: It turns out that 12 cm is the smallest length of wire that can be bent to
form an integer sided right angle triangle in exactly one way, but there are
many more examples.

  12 cm: (3, 4, 5)
  24 cm: (6, 8, 10)
  30 cm: (5, 12, 13)
  36 cm: (9, 12, 15)
  40 cm: (8, 15, 17)
  48 cm: (12, 16, 20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer
sided right angle triangle, and other lengths allow more than one solution to be
found; for example, using 120 cm it is possible to form exactly three different
integer sided right angle triangles.

  120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)

Given that L is the length of the wire, for how many values of L <= 1500000 can
exactly one integer sided right angle triangle be formed?

A: 161667
"""

from math import sqrt, gcd
from collections import defaultdict


def singular_integer_right_triangles(l):
    # Generate all Pythagorean triples with sum <= l
    # https://en.wikipedia.org/wiki/Pythagorean_triple
    #   a = k*(m^2 - n^2), b = k*(2*m*n), c = k*(m^2 + n^2)
    # where m > n > 0, k > 0, m and n coprime, m and n not both odd.
    # the formula generate all Pythagorean triples **uniquely**.
    # note the perimeter:
    #   a + b + c = k*2*m*(m + n) <= l
    # solve for m gives limit on m we need to search (k = 1):
    #   m <= (sqrt(2*l + 1) - 1)/2
    perimeter_to_num_solns = defaultdict(int)
    for m in range(2, int(0.5 * (sqrt(2 * l + 1) - 1)) + 1):
        for n in range(1, m):
            # exit conditions: m, n must be coprime; not both m, n odd
            if not gcd(m, n) == 1 or (m % 2 == 1 and n % 2 == 1):
                continue

            k = 1
            while True:
                a, b, c = (
                    k * (m**2 - n**2),
                    k * (2 * m * n),
                    k * (m**2 + n**2),
                )

                if a + b + c > l:
                    break

                # found a uniquely specified triple
                print(f"  perimeter = {a+b+c}, a={a} b={b} c={c}, m={m}, n={n}")
                perimeter_to_num_solns[a + b + c] += 1

                k += 1

    singular_solns = sum(cnt == 1 for cnt in perimeter_to_num_solns.values())

    return singular_solns


if __name__ == "__main__":
    L = 1500000
    print(
        f"Number of singular integer right triangles with perimeter less than"
        + f" or equal to{L}: {singular_integer_right_triangles(L)}"
    )
