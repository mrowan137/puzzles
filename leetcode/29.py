"""
Runtime: 36 ms, faster than 81.74% of Python3 online submissions for Implement strStr().
Memory Usage: 13.9 MB, less than 15.61% of Python3 online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] != needle[0]:
                continue

            j = i  # j is index in haystack
            k = 0  # k is index in needle
            while (
                j < len(haystack)
                and k < len(needle)
                and needle[k] == haystack[j]
            ):
                j += 1
                k += 1

            if j - i == len(needle):
                return i

        return -1
