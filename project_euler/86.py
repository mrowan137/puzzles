"""
Q: A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and
a fly, F, sits in the opposite corner. By travelling on the surfaces of the room
the shortest "straight line" distance from S to F is 10 and the path is shown on
the diagram.

        ________________ F
       /              /|
      /              / |
     /              /  |
    /              /   | 3
   /______________/    |
   |              |    |
   |              |    /
   |              |   /
   |              |  / 5
   |              | /
   |______________|/
  S
          6



However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring
rotations, with integer dimensions, up to a maximum size of M by M by M, for
which the shortest route has integer length when M = 100. This is the least
value of M for which the number of solutions first exceeds two thousand; the
number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one
million.

A: 1818
"""

from math import sqrt


def cuboid_short_route_is_int_length(a, b, c):
    # unfold the cube, draw a line from the corners
    shortest = min(
        sqrt((a + b) ** 2 + c**2),
        sqrt((a + c) ** 2 + b**2),
        sqrt((b + c) ** 2 + a**2),
    )
    return int(shortest) == shortest


def count_solutions(M, memo):
    # count number of integer-length shortest paths
    # considering up to a box of size MxMxM
    if M in memo:
        return memo[M]

    if M <= 1:
        return 0

    res = count_solutions(M - 1, memo)
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            res += cuboid_short_route_is_int_length(a, b, M)

    print(f"  -- {res} solutions")
    memo[M] = res
    return res


def main(target):
    M, memo = 1, {}
    while count_solutions(M, memo) < target:
        M += 1
        print(f"Trying M = {M}")

    return M


if __name__ == "__main__":
    TARGET = 1000000
    print(
        f"Smallest M for which {TARGET} cuboids have shortest"
        + f" corner-to-corner integral length: {main(TARGET)}"
    )
