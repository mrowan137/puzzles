"""
Runtime: 34 ms, faster than 80.84% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 73.33% of Python3 online submissions for Longest Common Prefix.
"""
# O(n log m), n is the number of strs and m is the length of smallest str
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs = sorted(strs, key=lambda s: len(s))
        longest = strs[0]
        l, r = 0, len(longest) - 1
        m = (l + r) // 2
        # search for the right idx
        while l <= r:
            m = (l + r) // 2
            if all(longest[: m + 1] == s[: m + 1] for s in strs):
                l = m + 1
            else:
                r = m - 1

        return longest[:l]


"""
Runtime: 940 ms, faster than 5.06% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 86.73% of Python3 online submissions for Longest Common Prefix.
"""
# brute force O(N*M), N is number of strings and M max length of a string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest, j = strs[0], 0
        for s in strs[1:]:
            for i in range(min(len(longest), len(s))):
                j = 0
                while j < len(s) and j < len(longest) and s[j] == longest[j]:
                    j += 1
            longest = s[:j]

        return longest
