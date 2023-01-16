"""
Q: If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.

A: 233168
"""


def sum_of_multiples(a, b, n):
    res = 0
    for i in range(n):
        res += i * (i % a == 0 or i % b == 0)

    return res


if __name__ == "__main__":
    print(
        "Sum of multiples of 3 or 5 below 1000: {}".format(
            sum_of_multiples(3, 5, 1000)
        )
    )
