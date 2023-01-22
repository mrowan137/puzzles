"""                                                                             
Q: The sum of the squares of the first ten natural numbers is,

  1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

  (1 + 2 + 3 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is

  3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

A: 25164150
"""


def difference(n):
    # we want to compute ( sum(1, n) )^2 - sum(1^2, n^2).
    # keep the difference small by subtracting out the second term at outset.
    # so compute the sum of (1 + 2 + ... + n)*(1 + 2 + .. + n) and skip if it's
    # a term like x*x.
    # how big would the final result be? it's certainly smaller than
    # sum(1, 100)^2 = 5050^2 ~= 25,000,000 which will not cause problems.
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            res += i * j

    return res


if __name__ == "__main__":
    n = 100
    print(
        "(1 + 2 + ... + {})^2 - (1^2 + 2^2 + ... + {}^2) = {}".format(
            n, n, difference(n)
        )
    )
