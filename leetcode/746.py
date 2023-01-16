"""
Runtime: 60 ms, faster than 48.77% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14.3 MB, less than 71.60% of Python3 online submissions for Min Cost Climbing Stairs.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)  # add dummy spot for last step
        for i in range(2, len(dp)):
            # cost to reach current is
            # 1. cost to reach i-1 (dp[i-1]) plus cost of i-1 (cost[i-1]),
            # or
            # 2. cost to reach i-2 (dp[i-2]) plus cost of i-2 (cost[i-2]),
            # whichever one is less.
            #
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]


"""
Runtime: 48 ms, faster than 97.94% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 14.5 MB, less than 46.65% of Python3 online submissions for Min Cost Climbing Stairs.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0] + [0] * (len(cost) - 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]
