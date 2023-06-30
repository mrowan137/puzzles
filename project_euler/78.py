"""
Q: Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5) = 7.

  OOOOO
  OOOO   O
  OOO   OO
  OOO   O   O
  OO   OO   O
  OO   O   O   O
  O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

A: 55374
"""
# By inspection we can notice a way to recursively build out the sequence:
# n:    0 | 1 |   2  |   3   |       4       |         5         |
#      ---|---|------|-------|---------------|-------------------|
#         | x | x x  | x x x | x x x x       | x x x x x         | build from n-1 by singlet
#         |   | xx   | xx x  | xx xx, x x xx | x x x xx, xx x xx | build from n-2 by doublet
#         |   |      | xxx   | x xxx         | x x xxx, xx xxx   | build from n-3 by triplet
#         |   |      |       | xxxx          | x xxxx            | build from n-4 by quadlet
#         |   |      |       |               | xxxxx             | build from n-5 by pentlet
#      ----------------------------------------------------------|
# p(n): 1 | 1 |   2  |   3   |       5       |         7         |
#
# The key observation is that any partition p(j) built from p(j - i), by adding
# a partition of size i, we need p(j - i) to be completely built of partitions
# size <i; if it's satisfied, we get p(j) by incrementing by p(j - i), for all
# possible i.
# Below implement the DP algorithm.
def calculate_partitions(n):
    # dp[i] represents partition function, p(i)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    # Outer loop builds by adding singlet, doublet, ...
    for i in range(n):
        # Inner loop builds p(j) from p(j - i), where i tracks singlet, doublet,
        # ...; by construction, p(j - i) has all possible builds from partitions
        # of size <i, and so adding a new partition of size i identifies all the
        # new partitions build from p(j - i)
        for j in range(1, n + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    return dp


def coin_partitions(target):
    # Manually choose it to be big enough
    n = 100000
    partitions = calculate_partitions(n)

    i = 1
    while i < len(partitions):
        if partitions[i] % target == 0:
            break

        i += 1

    res = (i, partitions[i]) if i <= n else None
    return res


if __name__ == "__main__":
    TARGET = 1000000
    RES = coin_partitions(TARGET)
    if RES:
        N, PARTITIONS = RES
        print(f"p({N}) = {PARTITIONS} is divisible by {TARGET}.")
    else:
        print("No solution found, increase search range.")
