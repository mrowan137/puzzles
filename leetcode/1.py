"""
Runtime: 48 ms, faster than 58.72% of Python3 online submissions for Two Sum.
Memory Usage: 15.7 MB, less than 11.76% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {target - n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            if n in diffs.keys() and i != diffs[n]:
                return i, diffs[n]
