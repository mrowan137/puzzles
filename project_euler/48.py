"""
Q: The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

A: 9110846700
"""


def last_m_digits(n, m):
    res = 0
    for i in range(n):
        partial = i + 1
        for _ in range(i):
            # compute i**i, storing just last 10 digits
            partial *= i + 1
            partial %= 10 ** m

        res += partial
        res %= 10 ** m

    return res


if __name__ == "__main__":
    n, m = 1000, 10
    print(
        "Last {} digits of 1^1 + 2^2 + 3^3 + ... + {}^{}: {}".format(
            m, n, n, last_m_digits(n, m)
        )
    )
