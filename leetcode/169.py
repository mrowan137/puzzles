"""
Runtime: 156 ms, faster than 92.22% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 78.63% of Python3 online submissions for Majority Element.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
