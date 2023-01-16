"""
Runtime: 44 ms, faster than 62.32% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.4 MB, less than 35.24% of Python3 online submissions for Unique Paths II.
"""
# dp -- O(MN)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[1][0] = 1
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                dp[j][i] = (dp[j - 1][i] + dp[j][i - 1]) * (
                    1 - obstacleGrid[j - 1][i - 1]
                )

        return dp[-1][-1]


"""
Runtime: 40 ms, faster than 84.34% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.3 MB, less than 83.41% of Python3 online submissions for Unique Paths II.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid[0]), len(obstacleGrid)

        # dp[j][i] is the number of ways to reach (i-1, j-1)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        # initial condition
        dp[0][1] = 1

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if obstacleGrid[j - 1][i - 1] != 1:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[-1][-1]
