"""
Q: n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

A: 648
"""


def multiply_by_n(number, n):
    # longhand multiply
    res = []
    sz = len(number)
    carry = 0
    for i in range(sz - 1, -1, -1):
        digit, carry = (
            (n * number[i] + carry) % 10,
            (n * number[i] + carry) // 10,
        )
        res.insert(0, digit)

    while carry:
        digit, carry = carry % 10, carry // 10
        res.insert(0, digit)

    return res


def factorial(n):
    res = [1]
    for i in range(1, n + 1):
        res = multiply_by_n(res, i)

    return res


if __name__ == "__main__":
    n = 100
    print("Sum of digits of {}!: {}".format(n, sum(factorial(n))))
