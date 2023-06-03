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

A: 661
"""

# Given:
#   x^2 - D*y^2 = 1
#   x^2 - (1 + D*y^2) = 0
# x, y are positive integers;
# D is a given positive integer;
# Find minimal solution in x.
#
# Brute force takes too long.
# Special equation, 'Pell Equation', which can be solved using continued
# fraction for sqrt(D).
# - https://mathworld.wolfram.com/DiophantineEquation2ndPowers.html
# - https://math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf

from math import sqrt, isqrt


def continued_fraction_representation_sqrt(D):
    """
    return continued fraction representation of sqrt(D)
    [a0, <a1, a2, ..., am>]
    """
    rep = []
    # starting point:
    #   b = a0, p = 1, sD := sqrt(D)
    #   p/( sD - b )
    #
    # complete the square:
    #   p*(sD + b)/ (sD**2 - b**2)
    #
    # simplify:
    #   (sD + b) / ((sD**2 - b**2)/p)
    #
    # extract next terms and iterate:
    #   p' = (sD**2 - b**2)/p
    #   b' = int(p/(sD - b))*p' - b
    sD = sqrt(D)
    a0 = int(sD)
    a = b = a0
    p = 1

    # done if 0 fractional part (i.e. D is a perfect square),
    # or if we reached the last term of the periodic part, 2*a0
    while a not in (sD, 2 * a0):
        rep.append(a)
        a = int(p / (sD - b))
        p = (D - b**2) / p
        b = a * p - b

    # the last term
    rep += [a0] if a == sD else [2 * a0]

    return rep


def pell_equation_solution(D):
    """
    return solution to Pell equation of form x^2 - D*y^2 = 1
    """

    # by assumption, no solution for D perfect square
    if isqrt(D) ** 2 == D:
        return None

    cf = continued_fraction_representation_sqrt(D)

    # initialize
    p0, p1 = 1, cf[0]
    q0, q1 = 0, 1

    # for period length l, minimal solution is given by
    #           { p_l-1, q_l-1,   l even
    # (x, y) =  |
    #           { p_2l-1, q_2l-1, l odd
    for a in cf[1:] + cf[1:]:
        p1, p0 = a * p1 + p0, p1
        q1, q0 = a * q1 + q0, q1

        if p0**2 - D * q0**2 == 1:
            return p0, q0

    return None


def answer(upper):
    res, largest_x = -1, -float("inf")

    for d in range(upper):
        soln = pell_equation_solution(d)

        if not soln:
            continue

        x, y = soln

        old = largest_x
        largest_x = max(x, largest_x)
        res = d if old != largest_x else res

        print(f"d = {d}, x = {x}, y = {y}, x^2 - D*y^2 = {x**2 - d*y**2}")

    return res


if __name__ == "__main__":
    UPPER = 1000
    print(
        f"For D <= {UPPER}, D = {answer(UPPER)}"
        + " gives largest x of minimal solutions in x, for x^2 - D*y^2 = 1."
    )
