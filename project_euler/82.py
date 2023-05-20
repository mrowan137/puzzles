"""
NOTE: This problem is a more challenging version of Problem 81.

Q: The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
the left column and finishing in any cell in the right column, and only moving
up, down, and right, is indicated in red and bold; the sum is equal to 994.

  131  673  234  103  18
  201  96   342  965  150
  630  803  746  422  111
  537  699  497  121  956
  805  732  524  37   331

Find the minimal path sum from the left column to the right column in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by
80 matrix.

A: 260324
"""


def path_sum(file_name):
    # read file
    matrix = []
    with open(file_name) as f:
        for line in f:
            row = line.replace("\n", "").split(",")
            matrix.append([int(x) for x in row])

    rows, cols = len(matrix), len(matrix[0])

    # two array to capture up and down directions, third for global min sum path
    dpu = [[float("inf") for _ in range(cols + 1)] for _ in range(rows + 1)]
    dpd = [[float("inf") for _ in range(cols + 1)] for _ in range(rows + 1)]
    dp = [[float("inf") for _ in range(cols + 1)] for _ in range(rows + 1)]

    # initialization
    for i in range(rows):
        dpu[i][0] = dpd[i][0] = dp[i][0] = 0

    # iterate columns in the outerloop
    # for up matrix, max comes from below or the left
    # for down matrix, max comes from above or the left
    for j in range(1, cols + 1):
        for i in range(1, rows + 1):
            k = rows - i
            dpd[i][j] = matrix[i - 1][j - 1] + min(dpd[i - 1][j], dp[i][j - 1])
            dpu[k][j] = matrix[k - 1][j - 1] + min(dpu[k + 1][j], dp[k][j - 1])

        # up and down matrices filled for a given j, fill global min
        for i in range(1, rows + 1):
            dp[i][j] = min(dpd[i][j], dpu[i][j])

    return min(dp[i][-1] for i in range(1, rows))


if __name__ == "__main__":
    print("Minimum path sum: {}".format(path_sum("./matrix.txt")))
