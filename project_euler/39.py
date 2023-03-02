"""
Q: If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

A: 840
"""

# constraints:
#   1. p = a + b + c --> c = a + b - p --> c^2 = (a + b)^2 - 2*p*(a + b) + p^2
#   2. c^2 = a^2 + b^2
#
# combine gives:
#   a^2 + b^2 = (a + b)^2 - 2*p*(a + b) + p^2
#           0 = 2*a*b - 2*p*(a + b) + p^2
#
# Solutions are:
#   p = (a + b) +/- sqrt( (a + b)^2 - 2*a*b )
#     = (a + b) +/- sqrt( a^2 + b^2 )
#
# Reject the '-' root because the perimeter will be larger than a + b.
# So the question can be rephrased as, which value of p admits
# the greatest number of solutions, where 3 <= p <= 1000
# and a and b are positive integers.
# Counting strategy is to iterate through valid values of a, b
# and increment the count of number of solutions.

from collections import defaultdict
from math import sqrt


def find_p_to_maximize_count_of_solutions():
    perimeter_to_count_of_solutions = defaultdict(int)
    for a in range(2, 500):
        for b in range(1, a):
            x, y = a + b, sqrt(a ** 2 + b ** 2)
            if 1.0 * int(y) != y:
                continue

            p = x + y

            if 3 <= p and p <= 1000:
                perimeter_to_count_of_solutions[p] += 1

    return max(
        perimeter_to_count_of_solutions, key=perimeter_to_count_of_solutions.get
    )


if __name__ == "__main__":
    print(
        "p = {:3.0f} (for p < 1000) maximizes number of solutions to ".format(
            find_p_to_maximize_count_of_solutions()
        )
        + "right triangle with integral-length sides."
    )
