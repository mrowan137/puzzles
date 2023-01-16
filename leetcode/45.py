"""
Runtime: 12527 ms, faster than 5.00% of Python3 online submissions for Jump Game II.
Memory Usage: 14.7 MB, less than 99.93% of Python3 online submissions for Jump Game II.
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [float(inf)] * (N)
        dp[0] = 0
        # dp[i+1] represents the min number of steps to reach step i

        for i in range(N):
            for j in range(1, min(nums[i] + 1, N - i)):
                dp[i + j] = min(dp[i + j], 1 + dp[i])

        return dp[N - 1]
