"""
Q: It is possible to show that the square root of two can be expressed as an
infinite continued fraction. By expanding this for the first four iterations, we
get:

  3/2, 7/5, 17/12, 41/29.

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than the denominator?

A: 153
"""

from math import log10


def num_digits(n):
    return int(log10(n)) + 1


def square_root_convergents(n):
    # find in the first n continued-fraction expansions of sqrt(2),
    # how many have numerator with more digits than denominator.
    # make the observation of recursive relationship:
    #
    #   num_m   2*num_{m-1} + num_{m-2}
    #   ----- = -----------------------
    #   den_m   2*den_{m-1} + den_{m-2}
    #
    # so we can use it and count cases where num digits
    # in the numerator exceeds that in the denominator
    num0, num1, num2 = 1, 1, 3
    den0, den1, den2 = 0, 1, 2
    cnt = 0
    for i in range(n):
        cnt += num_digits(num1) > num_digits(den1)
        num2, num1, num0 = 2 * num2 + num1, num2, num1
        den2, den1, den0 = 2 * den2 + den1, den2, den1

    return cnt


if __name__ == "__main__":
    N = 1000
    print(
        "Number of continued-fraction expansions to sqrt(2) (within first "
        + "{}), with more digits in numerator than denominator: {}".format(
            N, square_root_convergents(N)
        )
    )
