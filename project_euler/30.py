"""
Q: Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

A: 443839
"""


def sum_of_fifth_power_digits(n):
    res = 0
    while n:
        res += (n % 10) ** 5
        n //= 10

    return res


def digit_fifth_powers():
    # find the sum of all numbers that can be written as fifth power of digits.
    # the largest number to check is given by the constraint:
    #   m*9^5 >= 10^m - 1
    # where (positive integer) m is as large as possible.
    # --> m == 5
    res = 0
    for n in range(2, 5 * 9 ** 5):
        # ignore n == 1 because 1^5 is not a sum
        if sum_of_fifth_power_digits(n) == n:
            res += n

    return res


if __name__ == "__main__":
    print(
        "Sum of all numbers that can be "
        "written as fifth power of digits: {}".format(digit_fifth_powers())
    )
