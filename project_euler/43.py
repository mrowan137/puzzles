"""
Q: The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note
the following:

  d_2 d_3 d_4 = 406 is divisible by 2
  d_3 d_4 d_5 = 063 is divisible by 3
  d_4 d_5 d_6 = 635 is divisible by 5
  d_5 d_6 d_7 = 357 is divisible by 7
  d_6 d_7 d_8 = 572 is divisible by 11
  d_7 d_8 d_9 = 728 is divisible by 13
  d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

A: 16695334890
"""

from math import log10


def substring_divisible_pandigital(pd):
    # get a 0--9 pandigital pd, check it has the
    # substring divisible property
    divisors = [17, 13, 11, 7, 5, 3, 2]
    for i in range(7):
        right = pd % 1000
        if right % divisors[i] != 0:
            return False

        pd //= 10

    return True


def num_digits(n):
    if n == 0:
        return 1

    return 1 + int(log10(n))


def pad(n, d):
    # pad n with d zeros on the right
    if n == 0:
        return 0

    return n * 10 ** d


def pandigitals(n):
    # generate all n-digit pandigitals
    if n == 1:
        return [0]

    res = []
    for p in pandigitals(n - 1):
        # for each (n - 1)-digit pandigital, construct the n-digit
        # by inserting n in all possible locations

        d = num_digits(p)
        for i in range(d + 1):
            left = pad(p // (10 ** (d - i)), d - i + 1)
            mid = (n - 1) * 10 ** (d - i)
            right = p % (10 ** (d - i))
            new_pandigital = left + mid + right

            if num_digits(new_pandigital) == d + 1:
                res.append(new_pandigital)

    return res


def sum_substring_divisible_pandigitals():
    return sum(pd if substring_divisible_pandigital(pd) else 0
               for pd in pandigitals(10)
    )


if __name__ == "__main__":
    print(
        "Sum of all sub-string divisible 0--9 pandigitals: {}".format(
            sum_substring_divisible_pandigitals()
        )
    )
