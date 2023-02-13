"""
Q: By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)

A: 7273
"""

# The DP approach used in p18 is O(Nrows*max([len(row) for row in rows])),
# efficient enough to solve in a reasonable amount of time
def max_path_sum(numbers):
    # let dp[i][j] is the max sum in row i ending at entry j
    dp = []
    for row in numbers:
        dp.append([float("-inf") for _ in range(len(row))])

    # initialize
    dp[0][0] = numbers[0][0]

    # fill in the table
    for i, row in enumerate(dp):
        if i == 0:
            continue

        for j in range(len(dp[i])):
            dp[i][j] = (
                max(
                    dp[i - 1][min(j, len(dp[i - 1]) - 1)],
                    dp[i - 1][max(j - 1, 0)],
                )
                + numbers[i][j]
            )

    return max(dp[-1])


if __name__ == "__main__":
    numbers = []
    with open("triangle.txt") as f:
        for line in f:
            row = [int(n) for n in line.rstrip().replace(",", "").split(" ")]
            numbers.append(row)

    print("Maximum path sum: {}".format(max_path_sum(numbers)))
