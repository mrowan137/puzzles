"""
Runtime: 76 ms, faster than 30.39% of Python3 online submissions for Triangle.
Memory Usage: 15.3 MB, less than 25.08% of Python3 online submissions for Triangle.
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # initialize
        # dp[i] is the min sum possible up to that point
        dp = [[0] * len(row) for row in triangle]

        # iterate
        for j, row in enumerate(triangle):
            for i in range(len(row)):
                dp[j][i] = (
                    min(
                        dp[j - 1][max(i - 1, 0)],
                        dp[j - 1][min(i, len(triangle[j - 1]) - 1)],
                    )
                    + triangle[j][i]
                )

        return min(dp[-1])
