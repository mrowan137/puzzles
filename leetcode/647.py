"""
Runtime: 629 ms, faster than 11.60% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 22.1 MB, less than 25.16% of Python3 online submissions for Palindromic Substrings.
"""
# O(N^2) dynamic programming
class Solution:
    def countSubstrings(self, s: str) -> int:
        sz = len(s)

        # dp[i][j] says whether s[i:j+1] is a palindrome
        dp = [[False] * sz for _ in range(sz)]

        # a single letter is a palindrome
        for i in range(sz):
            dp[i][i] = True

        # recursive step: s[i:j+1] is palindrome if s[i+1][j-1] is palindrome
        # and if s[i] == s[j]
        for j in range(sz):
            for i in range(j):
                if j - 1 >= 0 and i + 1 < sz:
                    # outers match and inner is palindrome; or they're right next door
                    dp[j][i] = (dp[j - 1][i + 1] or j == i + 1) and s[i] == s[j]

        # count up the number of palindromes
        res = 0
        for j in range(sz):
            for i in range(j + 1):
                res += dp[j][i]

        return res


"""
Runtime: 9964 ms, faster than 5.01% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.3 MB, less than 46.06% of Python3 online submissions for Palindromic Substrings.
"""


class Solution:
    # brute force -- O(N^3)
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Check all possibilities -- iterate over all possible combos of being, end
        res = 0

        for i in range(len(s)):
            for j in range(i + 1):
                res += int(isPalindrome(s[j : i + 1]))

        return res
