"""
Runtime: 128 ms, faster than 82.03% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 59.68% of Python3 online submissions for Single Number.
"""
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use a hashmap: O(N) space, O(N) time
        # from collections import Counter
        # return {v:k for k,v in Counter(nums).items()}[1]

        # O(n) with no extra memory, properties of XOR
        # 1. XOR is commutative: a^b = b^a
        # 2. XOR satisfies a^a^b = b
        return reduce(lambda a, b: a ^ b, nums)
