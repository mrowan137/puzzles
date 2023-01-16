"""
Runtime: 4191 ms, faster than 11.75% of Python3 online submissions for Jump Game.
Memory Usage: 15.2 MB, less than 70.43% of Python3 online submissions for Jump Game.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(len(nums)):
            if dp[i]:
                jmax = min(nums[i], len(nums) - i - 1)
                dp[i + 1 : i + 1 + jmax] = [True] * jmax

        return dp[-1]
