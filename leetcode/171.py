"""
Runtime: 28 ms, faster than 90.04% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.2 MB, less than 42.60% of Python3 online submissions for Excel Sheet Column Number.
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle:
            return 0
        return (ord(columnTitle[0]) - 64) * 26 ** (
            len(columnTitle) - 1
        ) + self.titleToNumber(columnTitle[1:])
