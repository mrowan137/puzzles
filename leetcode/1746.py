"""
Runtime: 1120 ms, faster than 60.44% of Python3 online submissions for Maximum Subarray Sum After One Operation.
Memory Usage: 28.6 MB, less than 23.44% of Python3 online submissions for Maximum Subarray Sum After One Operation.
"""


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 1:
            return nums[0] ** 2
        dp = [[0] * sz for _ in range(2)]
        for i in range(sz):
            dp[0][i] = max(nums[i], nums[i] + dp[0][i - 1])
            dp[1][i] = max(
                nums[i],
                nums[i] + dp[1][i - 1],
                nums[i] * nums[i],
                nums[i] * nums[i] + dp[0][i - 1],
            )

        return max(dp[1])
