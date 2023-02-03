"""
Q: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

A: 1366
"""


def double(number):
    # calculate longhand then sum the digits
    sz = len(number)
    carry = 0
    for i in range(sz - 1, -1, -1):
        digit, carry = (
            (2 * number[i] + carry) % 10,
            (2 * number[i] + carry) // 10,
        )
        number[i] = digit

    while carry:
        digit, carry = carry % 10, carry // 10
        number.insert(0, digit)


def double_n_times(n):
    # compute 2^n
    res = [1]
    for _ in range(n):
        double(res)

    return res


if __name__ == "__main__":
    n = 1000
    print("Sum of digits of 2^{}: {}".format(n, sum(double_n_times(n))))
