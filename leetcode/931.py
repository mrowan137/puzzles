"""
Runtime: 124 ms, faster than 58.99% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 14.9 MB, less than 97.43% of Python3 online submissions for Minimum Falling Path Sum.
"""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        # dp[j][i] is the minimum sum possible up to the point dp[j][i]
        dp = [[0] * m for _ in range(n)]

        for j in range(n):
            for i in range(m):
                dp[j][i] = matrix[j][i] + min(
                    dp[j - 1][max(i - 1, 0)],
                    dp[j - 1][i],
                    dp[j - 1][min(i + 1, m - 1)],
                )

        return min(dp[-1])
