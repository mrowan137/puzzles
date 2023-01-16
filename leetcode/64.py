"""
Runtime: 140 ms, faster than 19.30% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.7 MB, less than 63.35% of Python3 online submissions for Minimum Path Sum.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid[0]) + 1, len(grid) + 1
        dp = [[0] * M for _ in range(N)]
        for j in range(1, N):
            dp[j][0] = float("inf")
        for i in range(1, M):
            dp[0][i] = float("inf")
        dp[1][0] = dp[0][1] = 0
        for i in range(1, M):
            for j in range(1, N):
                dp[j][i] = grid[j - 1][i - 1] + min(dp[j][i - 1], dp[j - 1][i])
        for row in dp:
            print(row)
        return dp[-1][-1]


"""
Runtime: 88 ms, faster than 97.67% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.7 MB, less than 62.75% of Python3 online submissions for Minimum Path Sum.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]

        # initial condition: allows dp[1][1] = grid[0][0]
        dp[0][1] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j][i] = grid[j - 1][i - 1] + min(dp[j][i - 1], dp[j - 1][i])

        return dp[-1][-1]
