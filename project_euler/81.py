"""
Q: In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red and
is equal to 2427.

Find the minimal path sum from the top left to the bottom right by only moving
right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K
text file containing an 80 by 80 matrix.

A: 427337
"""


def path_sum(file_name):
    # read file
    matrix = []
    with open(file_name) as f:
        for line in f:
            row = line.replace("\n", "").split(",")
            matrix.append([int(x) for x in row])

    rows, cols = len(matrix), len(matrix[0])

    # let dp[i][j] represents the minimum path sum ending in entry i,j
    dp = [[float("inf") for _ in range(cols + 1)] for _ in range(rows + 1)]

    # initialization
    dp[1][0] = dp[0][1] = 0

    # for entry (i, j), min path sum comes from above or left entry
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dp[i][j] = matrix[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    print("Minimum path sum: {}".format(path_sum("./matrix.txt")))
