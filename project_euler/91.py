"""
Q: The points P(x1, y1) and Q(x2, y2) are plotted at integer co-ordinates and
are joined to the origin, O(0, 0), to form triangle OPQ.

There are exactly fourteen triangles containing a right angle that can be formed
when each co-ordinate lies between 0 and 2 inclusive; that is,
0 <= x1, y1, x2, y2 >= 2.

Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

A: 14234
"""

from math import sqrt


def distance_squared(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def is_right_triangle(p0, p1, p2):
    if p0 == p1 or p0 == p2 or p1 == p2:
        return False

    asq, bsq, csq = (
        distance_squared(p0, p1),
        distance_squared(p0, p2),
        distance_squared(p1, p2),
    )

    # reassign based on who is hyp, if we got it wrong
    if asq > bsq >= csq or asq > csq >= bsq:
        # asq is hypotenuse
        csq, asq, bsq = asq, bsq, csq
    elif bsq > asq >= csq or bsq > csq >= asq:
        # bsq is hypotenuse
        csq, asq, bsq = bsq, asq, csq

    return asq + bsq == csq


def count_right_triangles_on_grid(m, n):
    points = [(i, j) for i in range(m + 1) for j in range(n + 1)]

    res, p0 = 0, (0, 0)
    for i, p1 in enumerate(points):
        print(f"p1: {i}/{len(points)-1}")
        j = i + 1
        while j < len(points):
            p2 = points[j]
            res += is_right_triangle(p0, p1, p2)
            j += 1

    return res


if __name__ == "__main__":
    M, N = 50, 50
    print(
        f"Number of right triangles on the grid of {M} x {N}:"
        + f" {count_right_triangles_on_grid(M, N)}"
    )
