"""
Runtime: 44 ms, faster than 79.27% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.2 MB, less than 82.59% of Python3 online submissions for Roman to Integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i, ans = 0, 0
        while i < len(s) - 1:
            a, b = d[s[i]], d[s[i + 1]]

            if a < b:
                ans += b - a
                i += 2
            else:
                ans += a
                i += 1

        # add the last
        if i == len(s) - 1:
            ans += d[s[i]]

        return ans
