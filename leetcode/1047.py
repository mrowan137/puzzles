"""
Runtime: 7928 ms
Memory Usage: 14.5 MB
"""


class Solution:
    def findDuplicate(self, s):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return (i, True)
        return (-1, False)

    def removeDuplicates(self, s: str) -> str:
        loop = True
        while loop:
            i, loop = self.findDuplicate(s)
            if loop:
                s = s[:i] + s[i + 2 :]

        return s
