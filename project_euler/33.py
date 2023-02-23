"""
Q: The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

A: 100
"""


def digit_cancelling_fractions():
    res = 1
    for i in range(1, 10):  # numerator 10s digit
        for j in range(1, 10):  # numerator 1s digit
            for k in range(1, 10):  # denominator 10s digit
                for l in range(1, 10):  # denominator 1s digit
                    num = 10 * i + j
                    den = 10 * k + l
                    f = num / den
                    if f < 1 and j != l:
                        # digit-cancelled possibilities for ij/kl
                        c1 = f == i / k and j == l  # i/k
                        c2 = f == i / l and j == k  # i/l
                        c3 = f == j / k and i == l  # j/k
                        c4 = f == j / l and i == k  # j/l
                        if c1 or c2 or c3 or c4:
                            print("{}{}/{}{}".format(i, j, k, l))
                            res *= den / num
    return res


if __name__ == "__main__":
    print(
        "Product of denominators of (lowest-terms) "
        "digit cancelling fractions: {}".format(digit_cancelling_fractions())
    )
