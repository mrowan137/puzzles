"""
Runtime: 218 ms, faster than 5.59% of Python3 online submissions for Implement strStr().
Memory Usage: 14.5 MB, less than 33.62% of Python3 online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        def checkIdx(i):
            return needle == haystack[i : i + len(needle)]

        for i in range(len(haystack)):
            if checkIdx(i):
                return i

        return -1
