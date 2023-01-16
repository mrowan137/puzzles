"""
Runtime: 40 ms, faster than 60.30% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.3 MB, less than 87.98% of Python3 online submissions for Running Sum of 1d Array.
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i + 1] + nums[i]

        return nums
