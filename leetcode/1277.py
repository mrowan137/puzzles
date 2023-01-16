"""
Runtime: 612 ms, faster than 65.83% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 16.9 MB, less than 15.37% of Python3 online submissions for Count Square Submatrices with All Ones.
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix[0]), len(matrix)

        # we define a dp matrix which stores
        # the number of squares that have a lower right corner in (i,j)
        dp = [[0] * (r + 1) for _ in range(c + 1)]
        for i in range(r):
            for j in range(c):
                if matrix[j][i]:
                    dp[j + 1][i + 1] = 1 + min(
                        dp[j][i], dp[j + 1][i], dp[j][i + 1]
                    )

        res = [sum(row) for row in dp]
        return sum(res)
