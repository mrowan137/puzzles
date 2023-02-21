"""
Q: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

  1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

A: 73682
"""


def coin_sums(amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # dp[i] is the number of ways to get to amount == i
    dp = [0] * (amount + 1)

    # initialization: one way to make 0p
    dp[0] = 1

    for c in coins:
        for i in range(1, amount + 1):
            # number of ways to get to amount i increments
            # by number of ways to get to amount i-c
            if i - c >= 0:
                dp[i] += dp[i - c]

    return dp[-1]


if __name__ == "__main__":
    ans = coin_sums(200)
    print("Number of ways to make £2 using coins: {}".format(ans))
