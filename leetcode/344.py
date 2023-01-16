"""
Runtime: 200 ms, faster than 37.36% of Python3 online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 55.84% of Python3 online submissions for Reverse String.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
