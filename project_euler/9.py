"""
Q: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

A: 31875000
"""


def find_pythagorean_triplet():
    # write c = 1000 - a - b. then we can loop over
    # b:[3, 1000], a:[1, b], and c is determined.
    for a in range(3, 1001):
        for b in range(1, a):
            c = 1000 - a - b
            if c <= b:
                continue

            if a**2 + b**2 == c**2:
                return (a, b, c)


if __name__ == "__main__":
    a, b, c = find_pythagorean_triplet()
    print("Pythagorean triplet: ({}, {}, {})".format(a, b, c))
    print("Product: {}".format(a * b * c))
