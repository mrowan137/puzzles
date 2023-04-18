"""
Q: By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles:

  x o o  x x o  x x x
  o o o  o o o  o o o
    6      4      2
  
  x o o  x x o  x x x
  x o o  x x o  x x x
    3      2      1

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.

A: 2772
"""


def count_rectangles(m, n, k):
    # fills out a grid `dp` of size m x n,
    # where the (i, j) element of the grid
    # gives the number of rectangles on:
    #   [0:i-1, 0:j-1], 1 <= i <= m, 1 <= j <= n
    # lastly, finds the coordinate that gives
    # rectangle count closest to k

    # initialize
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # count rectangles
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # i*j: the number of rectangles with
            #   a lower right corner at (i-1, j-1)
            # dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]:
            #   number of rectangles in the region that
            #   excludes the cell at (i-1, j-1)
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + i * j

    # it's filled in, iterate and find value closest to k
    residual = float("inf")
    area = -1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            old_residual = residual
            residual = min(residual, abs(k - dp[i][j]))
            if residual < old_residual:
                area = i * j

    return area


if __name__ == "__main__":
    # rough guess, m = 1000, n = 1000 will have enough
    M = N = 1000
    K = 2000000
    print(
        "Area of grid with number of rectangles closest to {}: {}".format(
            K, count_rectangles(M, N, K)
        )
    )
