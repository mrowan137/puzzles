"""
Runtime: 92 ms, faster than 86.13% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.7 MB, less than 8.12% of Python3 online submissions for First Unique Character in a String.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(list(s))
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
