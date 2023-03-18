"""
Q: There are exactly ten ways of selecting three from five, 12345:

  123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, Choose(5, 3) = 10.

In general, Choose(n, r) = n!/(r!(n-r)!), where  r <= n, n! = n*(n-1)*...*1, and
0! = 1. It is not until n = 23, that a value exceeds one-million:
  
  Choose(23, 10) = 1144066.

How many, not necessarily distinct, values of Choose(n, r) for 1 <= n <= 100,
are greater than one-million?

A: 4075
"""


def combinatoric_selections(m, max_depth):
    # compute how many combinatoric selections Choose(n, r) exceed m,
    # considering up to max_depth levels into Fibonacci tree.
    # return signature: node value, how many nodes greater than m (res)

    # initial state: n = 1 level of Fibonacci tree
    level, res = [0, 1, 1, 0], 0
    for i in range(max_depth):
        # sum contributions from this level
        res += sum(v > m for v in level)

        # construct the next level
        next_level = []
        for i in range(len(level) - 1):
            # inf is a marker for the value is bigger than m
            to_add = level[i] + level[i + 1]
            to_add = to_add if to_add < m else float("inf")
            next_level.append(to_add)

        level = [0] + next_level + [0]

    return res


if __name__ == "__main__":
    M, MAX_DEPTH = 1000000, 100
    print(
        "Number of values Choose(n, r), 1 <= n <= {}, greater than {}: ".format(
            MAX_DEPTH, M
        )
        + "{}".format(combinatoric_selections(M, MAX_DEPTH))
    )
