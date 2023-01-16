"""
Runtime: 36 ms, faster than 57.75% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 14.2 MB, less than 44.43% of Python3 online submissions for Number of Good Pairs.
"""
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        for v in c.values():
            res += (v - 1) * v // 2
        return sum(map(lambda x: (x - 1) * x // 2, [v for v in c.values()]))
