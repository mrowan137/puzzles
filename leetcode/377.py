"""
Runtime: 40 ms, faster than 74.08% of Python3 online submissions for Combination Sum IV.
Memory Usage: 14.4 MB, less than 45.92% of Python3 online submissions for Combination Sum IV.
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = target

        # dp[i] is the number of combinations add to i
        dp = [0] * (N + 1)
        dp[0] = 1

        for i in range(1, N + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]

        return dp[-1]
