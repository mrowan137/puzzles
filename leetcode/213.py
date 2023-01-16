"""
Runtime: 32 ms, faster than 65.18% of Python3 online submissions for House Robber II.
Memory Usage: 14 MB, less than 94.36% of Python3 online submissions for House Robber II.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sz = len(nums)
        dp0 = [0] * (sz) + [0] * 2
        dp1 = [0] * (sz) + [0] * 2

        # compute considering you robbed the first or second
        for i in range(sz - 1):
            dp0[i] = max(dp0[i - 1], nums[i] + dp0[i - 2])
            dp1[i + 1] = max(dp1[i], nums[i + 1] + dp1[i - 1])

        return max(max(dp0), max(dp1))


"""
Runtime: 45 ms, faster than 16.14% of Python3 online submissions for House Robber II.
Memory Usage: 14.3 MB, less than 25.06% of Python3 online submissions for House Robber II.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def _rob(nums):
            N = len(nums)
            dp = [0, nums[0]] + [0] * (N - 1)
            dp[0], dp[1] = 0, nums[0]
            for i in range(2, N + 1):
                dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
            return dp[N]

        return max(_rob(nums[1:]), _rob(nums[: len(nums) - 1]))
