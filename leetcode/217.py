"""
Runtime: 112 ms, faster than 90.52% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.6 MB, less than 22.02% of Python3 online submissions for Contains Duplicate.
"""
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any([v >= 2 for v in Counter(nums).values()])
