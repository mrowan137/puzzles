"""
Q: All square roots are periodic when written as continued fractions and can be
written in the form:

  sqrt(N) = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...))) 
 
For example, let us consider sqrt(23):

  sqrt(23) = 4 + sqrt(23) - 4
           = 4 + 1/(1/(sqrt(23) - 4))
           = 4 + 1/(1 + (sqrt(23) - 3)/7)

If we continue we would get the following expansion:

  sqrt(23) = 4 + 1/(1 + 1/(3 + 1/(1 + 1/(8 + ...))))
 
The process can be summarised as follows:

  a0 = 4, 1/(sqrt(23) - 4) = (sqrt(23) + 4)/7
  a1 = 1, 7/(sqrt(23) - 3) = 7*(sqrt(23) + 3)/14
  a2 = 3, 2/(sqrt(23) - 3) = 2*(sqrt(23) + 3)/14
  a3 = 1, 7/(sqrt(23) - 4) = 7*(sqrt(23) + 4)/7
  a4 = 8, 1/(sqrt(23) - 4) = (sqrt(23) + 4)/7
  a5 = 1, 7/(sqrt(23) - 3) = 7*(sqrt(23) + 3)/14
  a6 = 3, 2/(sqrt(23) - 3) = 2*(sqrt(23) + 3)/14
  a7 = 1, 7/(sqrt(23) - 4) = 7*(sqrt(23) + 4)/7


It can be seen that the sequence is repeating. For conciseness, we use the
notation sqrt(23) = [4; (1,3,1,8)], to indicate that the block (1,3,1,8)
repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

  sqrt(2) = [1; (2)], period = 1
  sqrt(3) = [1; (1,2)], period = 2
  sqrt(5) = [2; (4)], period = 1
  sqrt(6) = [2; (2,4)], period = 2
  sqrt(7) = [2; (1,1,1,4)], period = 4
  sqrt(8) = [2; (1,4)], period = 2
  sqrt(10) = [3; (6)], period = 1
  sqrt(11) = [3; (3,6)], period = 2
  sqrt(12) = [3; (2,6)], period = 2
  sqrt(13) = [3; (1,1,1,1,6)], period = 5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?

A: 1322
"""

from math import sqrt


def continued_fraction_representation(n):
    rep = []
    # starting point:
    #   b = a0, p = 1, sn := sqrt(n)
    #   p/( sn - b )
    #
    # complete the square:
    #   p*(sn + b)/ (sn**2 - b**2)
    #
    # simplify:
    #   (sn + b) / ((sn**2 - b**2)/p)
    #
    # extract next terms and iterate:
    #   p' = (sn**2 - b**2)/p
    #   b' = int(p/(sn - b))*p' - b
    sn = sqrt(n)
    a0 = int(sn)
    a = b = a0
    p = 1

    # done if 0 fractional part (i.e. n is a perfect square),
    # or if we reached the last term of the periodic part, 2*a0
    while a not in (sn, 2 * a0):
        rep.append(a)
        a = int(p / (sn - b))
        p = (n - b**2) / p
        b = a * p - b

    # the last term
    rep += [a0] if a == sn else [2 * a0]

    return rep


def odd_period_continued_fractions(n):
    # background:
    #   we can use a known result about periodic continued fractions,
    #   e.g. https://mathworld.wolfram.com/PeriodicContinuedFraction.html:
    #      ```
    #      periodic part of continued fraction (excluding last term) is
    #      mirror symmetric, e.g. of the form [a0, a1, a2, ..., a2, a1, 2*a0]
    #      ```
    #
    # strategy:
    #   generate the sequence of continued fractions numbers,
    #   [a0, a1, a2, ..., a2, a1, 2*a0], stopping at 2*a0; count
    #   the length of the period
    cnt = 0
    for i in range(1, n + 1):
        print(i)
        cnt += len(continued_fraction_representation(i)) % 2 == 0

    return cnt


if __name__ == "__main__":
    N = 10000
    print(
        "Number of odd-period continued fractions less than or equal to "
        + f"{N}: {odd_period_continued_fractions(N)}"
    )
