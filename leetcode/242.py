"""
Runtime: 20 ms, faster than 99.99% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 34.23% of Python3 online submissions for Valid Anagram.
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
