"""
Q: A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?

A: 972
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


def powerful_digital_sum():
    # direct computation with longhand multiply
    res = float("-inf")
    for a in range(100):
        a_times_b = [1]
        for b in range(100):
            a_times_b = multiply_by_n(a_times_b, a)
            res = max(res, sum(a_times_b))

    return res


if __name__ == "__main__":
    print(
        "Maximum digital sum of a^b, "
        + "where a, b < 100: {}".format(powerful_digital_sum())
    )
