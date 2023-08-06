"""
Q: It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has an
area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral
side lengths and area and whose perimeters do not exceed one billion
(1 000 000 000).

A: 518408346
"""

from decimal import Decimal


# not thrilled with this approach but it gets the job done..
def isosceles_area(x, y):
    # give the area of isosceles triangle; x is the side
    # length of two equal sides, y is remaining side

    x, y = Decimal(x), Decimal(y)

    # Heron's formula
    half_perimeter = (Decimal(2) * x + y) / Decimal(2)
    a = (
        half_perimeter
        * (half_perimeter - x) ** Decimal(2)
        * (half_perimeter - y)
    )
    return a


def is_integer(x):
    # we use this on `Decimal` types after high-precision calculation;
    # `Decimal` does not have built-in `is_integer` method
    return x == int(x)


def sum_perimeters_almost_eq_triangles(max_perimeter):
    res = 0
    for s in range(3, max_perimeter // 3 + 1):
        if s % 1000000 == 0:
            print(f"completion: {round(100.*s/(max_perimeter//3 + 1), 3)}%")

        a1, a2 = (isosceles_area(s, s + 1), isosceles_area(s, s - 1))

        # only count if perimeter is within the range
        res += is_integer(a1.sqrt()) * (3 <= 3 * s + 1 < max_perimeter) * (
            3 * s + 1
        ) + is_integer(a2.sqrt()) * (3 <= 3 * s - 1 < max_perimeter) * (
            3 * s - 1
        )

    return res


if __name__ == "__main__":
    M = 1000000000
    print(
        "Sum of the perimeters of all almost equilateral triangles "
        + "with integral side lengths and area and whose perimeters "
        + f"do not exceed: {M}: {sum_perimeters_almost_eq_triangles(M)}"
    )
