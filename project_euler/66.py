"""
Q: Consider quadratic Diophantine equations of the form:
  x - D*y^2 = 1
For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is
square. By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:
  3^2 - 2*2^2 = 1
  2^2 - 3*1^2 = 1
  9^2 - 5*4^2 = 1
  5^2 - 6*2^2 = 1
  8^2 - 7*3^2 = 1
 
Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D = 5.

Find the value of D in minimal solutions of x for which the largest value of x
is obtained.

A: 
"""

# Given:
#   x^2 - D*y^2 = 1
#   x^2 - (1 + D*y^2) = 0
# x, y are positive integers;
# D is a given positive integer;
# Find minimal solution in x.
#
# Quadratic formula:
#   x = sqrt( 1 + D*y^2 )
#
# Let's test it out:
#   D = 2:
#   x = sqrt( 1 + 2*y^2 )
#
# Count upward from y = 1 shows x = sqrt(9) = 3 is the minimal solution.
# So we can count from y = 1 until get to x is an integer.
# It will be the minimal since sqrt(n) is monotonically increasing.

import decimal
from math import sqrt


decimal.getcontext().prec = 20


def diophantine(D):
    largest_x = -float("inf")
    res = -1
    for d in range(2, D + 1):
        # no solutions in positive integers when d is square
        if sqrt(d) == int(sqrt(d)):
            continue

        y = decimal.Decimal(1)
        while True:
            y += decimal.Decimal(1)
            x_squared = (
                decimal.Decimal(1)
                + decimal.Decimal(d) * decimal.Decimal(y) ** 2
            )

            if int(sqrt(x_squared)) ** 2 == x_squared:
                break

        old = largest_x
        largest_x = max(sqrt(x_squared), largest_x)
        res = d if old != largest_x else res

        print(
            f"d = {d}, x = {sqrt(x_squared)}, y = {y}, x^2 - D*y^2 = {x_squared - d*y**2}"
        )

    return res


if __name__ == "__main__":
    upper = 1000
    print(
        f"For D <= {upper}, D = {diophantine(upper)}"
        + " gives largest x of minimal solutions in x, for x^2 - D*y^2 = 1."
    )
