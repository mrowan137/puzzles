"""
Runtime: 116 ms, faster than 98.76% of Python3 online submissions for Missing Number.
Memory Usage: 15.3 MB, less than 79.69% of Python3 online submissions for Missing Number.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
