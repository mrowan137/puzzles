"""
Runtime: 36 ms, faster than 83.62% of Python3 online submissions for Arithmetic Slices.
Memory Usage: 14.6 MB, less than 43.94% of Python3 online submissions for Arithmetic Slices.

Insight: dp[i] stores the number of arithmetic slices in the first i elems. We
have a variable length that tracks the current length ( - 2) of the arithmetic
slices; each time we add a new elem to the end of the current, it adds length+1
to the current count, e.g. 1 2 3 length = 1, add a 4, now length = 2 for the two
new slices we can add. [1 2 3 4], 1 [2 3 4] reset length if we break the sequence.
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)

        # definition
        dp = [
            0
        ] * N  # dp[i] is the number of arithmetic slices considering the first i elems

        # initialization
        dp[0] = 0  # 0 arithmetic slice in the first 0 elems

        # iterate
        length = 0
        for i in range(2, N):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                length += 1
            else:
                length = 0

            dp[i] = dp[i - 1] + length

        return dp[-1]
