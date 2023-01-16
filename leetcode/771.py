"""
Runtime: 32 ms, faster than 69.54% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14.2 MB, less than 44.84% of Python3 online submissions for Jewels and Stones.
"""
from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s, j = Counter(stones), Counter(jewels)
        return sum([s[jewel] for jewel in j])
