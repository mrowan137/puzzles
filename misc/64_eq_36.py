"""
Q: Can we find a number system (base) where 36 == 64?
A: No, unfortunately
"""
import numpy as np


def check(b1, b2):
    # b1, b2 are the base of the two number systems
    return b1, b2, 3 * b1 ** 1 + 6 * b1 ** 0 == 6 * b2 ** 1 + 4 * b2 ** 0


def search():
    # Searh only up to base 10, because we would run out of digits
    for i in range(100):
        for j in range(100):
            b1, b2, res = check(i, j)
            if res:
                print("36 in base {} == 64 in base {}".format(b1, b2))
                return

    print("No base where 36 == 64")


if __name__ == "__main__":
    search()
