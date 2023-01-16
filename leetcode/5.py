"""
Runtime: 4475 ms, faster than 15.89% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 91.31% of Python3 online submissions for Longest Palindromic Substring.
"""


class Solution:
    # O(N^2)-ish
    def longestPalindrome(self, s: str) -> str:
        # insight: each letter or space can be the start of a odd or even palindrome
        sz = len(s)

        res = ""
        for i in range(2 * sz - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < sz and s[l] == s[r]:
                res = max(res, s[l : r + 1], key=len)
                l -= 1
                r += 1

        return res


"""
Runtime: 9948 ms, faster than 5.02% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22.1 MB, less than 7.84% of Python3 online submissions for Longest Palindromic Substring.
"""
# dp O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)

        dp = [[False] * sz for i in range(sz)]

        for i in range(sz):
            dp[i][i] = True

        for j in range(sz):
            for i in range(j + 1):
                if i + 1 < sz and j - 1 >= 0:
                    if (dp[j - 1][i + 1] or i == j - 1) and s[i] == s[j]:
                        dp[j][i] = True

        i_max, j_max = None, None
        m = float("-inf")
        for j in range(sz):
            for i in range(j + 1):
                if dp[j][i] and j - i + 1 > m:
                    i_max, j_max = i, j
                    m = j - i + 1

        return s[i_max : j_max + 1]


"""
Runtime: 7336 ms, faster than 14.92% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 22.1 MB, less than 12.52% of Python3 online submissions for Longest Palindromic Substring.
"""
# dp -- O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        # dp[j][i] true represents s[i:j+1] is palindrome
        dp = [[False] * (N) for _ in range(N)]

        # initialize: every char is a palindrome
        for i in range(N):
            dp[i][i] = True

        # fill the dp in a way that all required subproblem are satisfied
        # note j > i and we refer to j-1, i+1 as the subproblems
        # therefore j goes left to right, i goes right to left
        res = s[0]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                # I might be a palindrome if outer letters match
                if s[i] == s[j]:
                    # I am definitely a palindrome if inner is palindrome or we're neighbors
                    dp[j][i] = dp[j - 1][i + 1] or j == i + 1
                    if dp[j][i]:
                        res = (
                            s[i : j + 1]
                            if len(s[i : j + 1]) > len(res)
                            else res
                        )

        return res


"""
Runtime: 1136 ms, faster than 53.84% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 82.72% of Python3 online submissions for Longest Palindromic Substring.
"""
# recursion -- O(N^2) but generally better than dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(s, l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                r += 1
                l -= 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            res = max([res, getPalindrome(s, i, i)], key=len)
            res = max([res, getPalindrome(s, i, i + 1)], key=len)
        return res
