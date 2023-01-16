"""
Runtime: 52 ms, faster than 92.47% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.3 MB, less than 73.18% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
"""
from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        c = Counter(nums)

        res = [0] * sz

        d = {}
        tmp = 0

        for n in sorted(c.keys()):
            d[n] = tmp
            tmp += c[n]

        for i, n in enumerate(nums):
            res[i] = d[n]

        return res
