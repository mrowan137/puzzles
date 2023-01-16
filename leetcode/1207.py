"""
Runtime: 79 ms, faster than 10.37% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 13.9 MB, less than 72.38% of Python3 online submissions for Unique Number of Occurrences.
"""
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return 1 == max(Counter(Counter(arr).values()).values())
