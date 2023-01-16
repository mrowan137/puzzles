"""
Runtime: 1480 ms, faster than 57.11% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 24.8 MB, less than 48.92% of Python3 online submissions for Range Sum Query 2D - Immutable.
"""


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix[0]), len(matrix)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j][i] = (
                    dp[j][i - 1]
                    + dp[j - 1][i]
                    - dp[j - 1][i - 1]
                    + matrix[j - 1][i - 1]
                )

        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        col1 += 1
        col2 += 1
        row1 += 1
        row2 += 1
        return (
            self.dp[row2][col2]
            - self.dp[row2][col1 - 1]
            - self.dp[row1 - 1][col2]
            + self.dp[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
