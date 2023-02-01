"""
Q: Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

A: 137846528820
"""

from math import comb


def count_routes(m, n):
    # we can use math approach: from m + n steps to reach the bottom corner,
    # choose m of them to be the vertical step, and remaining n are determined
    return comb(m + n, m)


if __name__ == "__main__":
    m, n = 20, 20
    print(
        "Number of ways to reach bottom right corner of "
        "{} x {} grid, starting from the upper left: {}".format(
            m, n, count_routes(m, n)
        )
    )
