"""
Runtime: 52 ms, faster than 95.02% of Python3 online submissions for Paint House.
Memory Usage: 14.4 MB, less than 57.41% of Python3 online submissions for Paint House.
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])

        M, N = len(costs[0]), len(costs)
        dp = [[0] * M for _ in range(N)]

        for j in range(N):
            for i in range(M):
                dp[j][i] = (
                    min(dp[j - 1][(i + 1) % 3], dp[j - 1][(i - 1) % 3])
                    + costs[j][i]
                )

        return min(dp[-1])
