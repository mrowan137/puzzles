"""
Q: It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

A: 190569291
"""


def count_summations(n):
    # dp[i] represents the number of ways to express i
    # using the values 1, 2, ..., i, in increasing order
    dp = [0] * (n + 1)
    dp[0] = 1

    # fix backtrack distance, and consider for each value the number of ways
    # it is expressed in summation; building in this sequence from
    # left --> right ensures that dp[j-i] is updated by the time it is needed to
    # update dp[j], essentially keeping the chosen summations ordered from small
    # to large values
    # e.g. n = 4:
    #   1 0 0 0 0
    #   1 1 1 1 1  (+dp[j-1]; build using 1s)
    #   1 1 2 2 3  (+dp[j-2]; build using 1s, 2s)
    #   1 1 2 3 4  (+dp[j-3]; build using 1s, 2s, 3s)
    for i in range(n):
        for j in range(1, n + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    return dp[-1]


if __name__ == "__main__":
    N = 100
    print(
        "{} can be written as sum of at least 2 positive integers in {} ways".format(
            N, count_summations(N)
        )
    )
