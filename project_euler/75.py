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

A: 
"""

from math import isqrt, sqrt
from collections import defaultdict

def singular_integer_right_triangles(l):
    perimeter_to_num_solns = defaultdict(int)

    # iterate all possible right trangle with perimeter <= l, increment count
    # Notes:
    #   a + b + c <= l
    #   a^2 + b^2 == c^2
    #   a + b + sqrt(a^2 + b^2) <= l
    # Solve for b gives limit in b:
    #   b <= (l/2)*(2*a - l)/(a - l)
    for a in range(1, l):
        print(f"a = {a} / a_max = {l -1}")
        for b in range(a, int((l/2)*(2*a - l)/(a - l)) + 1):
            c_sqrt, c_isqrt = sqrt(a**2 + b**2), isqrt(a**2 + b**2)
            #print(f"  perimeter = {a+b+c_sqrt}, a={a} b={b} c={c_sqrt}")
            if c_sqrt == c_isqrt:
                perimeter_to_num_solns[a + b + c_isqrt] += 1

    singular_solns = sum(cnt == 1 for cnt in perimeter_to_num_solns.values())
            
    return singular_solns


if __name__ == "__main__":
    L = 1500000
    print(
        f"Answer: {singular_integer_right_triangles(L)}"
    )
