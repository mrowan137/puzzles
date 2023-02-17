"""
Q: Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

A: 669171001
"""

import math


def spiral_diagonals_sum(N):
    # count the sum of diagnoal elements in a square of size NxN
    # observation: NxN square is created out of N//2 + 1 spirals
    # and the upper right corners is equal to (s+1)^2, where
    # s := 2*(i - 1), for the ith spiral (i > 1); the sum of
    # corners is then:
    #   4*(s + 1)^2 - (1*s + 2*s + 3*s)
    # so compute the sum as groups of 4 corners
    res = 0
    for i in range(1, (N // 2 + 1) + 1):
        if i == 1:
            res += 1
            continue

        s = 2 * (i - 1)
        res += 4 * (s + 1) ** 2 - 6 * s

    return res


if __name__ == "__main__":
    N = 1001
    print("Sum of spiral diagonals: {}".format(spiral_diagonals_sum(N)))
