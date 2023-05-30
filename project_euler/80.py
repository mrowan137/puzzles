"""
Q: It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots is
infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880, and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots.

A: 40886
"""

from math import sqrt, log10
import decimal


def newton_raphson_square_root(a, num_digits):
    # Newton-raphson to compute square root of `a`
    # to given number of decimal digits of precision:
    # x_{n+1} = 0.5*(x_n + a/x_n) = x_n * (1 + a/x_n^2)/2
    decimal.getcontext().prec = num_digits + 2
    prec = decimal.Decimal(10) ** decimal.Decimal(
        -1 * (num_digits - (1 + int(log10(a))) + 1)
    )

    # take a/2 as initial guess for sqrt(a)
    a_prec = decimal.Decimal(a)
    approx = decimal.Decimal(0.5) * a_prec

    while abs(a_prec - approx**2) > prec:
        approx *= decimal.Decimal(0.5) * (
            decimal.Decimal(1) + a_prec / approx**2
        )

    return approx


def sqrt_digital_expansion(num_digits):
    # sum up the decimal digits of first 100
    # natural numbers, to 100 digits precision
    res = 0

    for i in range(1, 101):
        # just the irrationals
        if sqrt(i) != int(sqrt(i)):
            digits = newton_raphson_square_root(i, num_digits)
            res += sum(
                int(d) for d in str(digits).replace(".", "")[:num_digits]
            )

    return res


if __name__ == "__main__":
    NUM_DIGITS = 100
    print(
        f"Digital sum of first {NUM_DIGITS} digits for sqrt of "
        + f"first 100 natural numbers: {sqrt_digital_expansion(NUM_DIGITS)}"
    )
