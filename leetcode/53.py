"""
Runtime: 64 ms, faster than 72.84% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15.1 MB, less than 34.28% of Python3 online submissions for Maximum Subarray.

explanation:
test case:  [1,2,3,-2,4]
window_sum: [1,3,6, 4,8]  --> don't restart the window b/c pos;
                              still contribute to the max window
max_sum:    [1,3,6, 6,8]

test case:  [1,2,3,-7,4]
window_sum: [1,3,6, 0,4]
max_sum:    [1,3,6, 6,4]
can also see as dp: dp[i] is the maximum subarray ending at i
so dp[i] = dp[i-1] + nums[i] if pos > 0 else 0
Note: do not reset the window when window sum decreases
because any positive sum can still contribute to the max sum
reset only if the window sum is negative, since that can never
contribute to the max sum
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]

        return max(dp)


"""
Runtime: 752 ms, faster than 59.95% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.2 MB, less than 81.38% of Python3 online submissions for Maximum Subarray.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sz = len(nums)
        dp = [float("-inf")] * sz

        for i in range(sz):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


"""
TLE
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # recursion? too slow
        # exit condition
        if len(nums) == 1:
            return nums[0]

        res = max(
            sum(nums), self.maxSubArray(nums[1:]), self.maxSubArray(nums[:-1])
        )

        return res
