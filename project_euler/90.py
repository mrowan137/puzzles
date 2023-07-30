"""
Q: Each of the six faces on a cube has a different digit (0 to 9) written on it;
the same is done to a second cube. By placing the two cubes side-by-side in
different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
    ________    ________
   /       /|  /       /|
  /_______/ | /_______/ |
  |       | | |       | |
  |   6   | / |   4   | /
  |_______|/  |_______|/   


In fact, by carefully choosing the digits on both cubes it is possible to
display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49,
64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so
that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for
all nine square numbers to be displayed; otherwise it would be impossible to
obtain 09.

In determining a distinct arrangement we are interested in the digits on each
cube, not the order.
  {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
  {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the
last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square
numbers to be displayed?

A: 1217
"""

from math import sqrt
from itertools import combinations


def arrangement_shows_all_squares(cube1, cube2):
    nums = [10 * tens + ones for tens in cube1 for ones in cube2]
    nums += [10 * tens + ones for tens in cube2 for ones in cube1]
    nums = set(nums)

    # don't count 0 as a two-digit square
    if 0 in nums:
        nums.remove(0)

    # check if the cubes generate squares: 01, 04, 09, 16, 25, 36, 49, 64, 81
    res = sum(int(sqrt(x)) == sqrt(x) for x in nums) == 9
    return res


def cube_digit_pairs():
    # generate all possible ways to number a cube
    digits = list(range(10))
    combos = combinations(digits, 6)
    combos = [set(c) for c in combos]

    # treat 6 and 9 as equivalent
    for c in combos:
        if 6 in c:
            c.add(9)
        if 9 in c:
            c.add(6)

    # count distinct arrangements of the two cubes shoinwg the two-digit squares
    res = 0
    for i, cube1 in enumerate(combos):
        for cube2 in combos[i:]:
            res += arrangement_shows_all_squares(cube1, cube2)

    return res


if __name__ == "__main__":
    print(f"Number of distinct arrangements: {cube_digit_pairs()}")
