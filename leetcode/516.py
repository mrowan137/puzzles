"""
Runtime: 3097 ms, faster than 21.76% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.8 MB, less than 73.17% of Python3 online submissions for Longest Palindromic Subsequence.
"""
# O(N^2) -- dp
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sz = len(s)

        # d[j][i] is the length of longest palindromic subseq between i:j+1
        dp = [[0] * sz for _ in range(sz)]

        # a single letter is a palindromic subsequence of length 1
        for i in range(sz):
            dp[i][i] = 1

        # iterating through letter, then backwards from that letter
        for j in range(sz):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:  # for matching letters,
                    dp[j][i] = (
                        2 + dp[j - 1][i + 1]
                    )  # add 2 and take inner subseq
                    # this is okay because
                    # s[i:i+1] will have dp[i+1][i]
                    # above the diagonal which is 0s
                else:  # with no match, take whichever
                    dp[j][i] = max(
                        dp[j][i + 1],  # is larger subsequence, chopping
                        dp[j - 1][i],
                    )  # left or rightmost letter

        return dp[-1][0]


"""
Runtime: 2256 ms, faster than 45.42% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.8 MB, less than 74.98% of Python3 online submissions for Longest Palindromic Subsequence.
"""
# dp O(N^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        # dp[j][i] is the longest subsequence between i and j
        # Set initial conditions; 1 for i == j, 0 if i > j
        dp = [[None] * N for _ in range(N)]
        for j in range(N):
            for i in range(N):
                if i == j:
                    dp[j][i] = 1
                if j < i:
                    dp[j][i] = 0

        # Iterate in a way that ensures the required subproblems are solved already
        for j in range(1, N):
            for i in range(j - 1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = 2 + dp[j - 1][i + 1]
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i + 1])

        return dp[N - 1][0]


"""
TLE
"""
# Recursion O(N^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        if s[0] == s[-1]:
            return 2 + self.longestPalindromeSubseq(s[1:-1])
        else:
            return max(
                self.longestPalindromeSubseq(s[1:]),
                self.longestPalindromeSubseq(s[:-1]),
            )


"""
TLE
"""
# simple recursion
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        def lps(i, j):
            if i == j:
                return 1
            if j < i:
                return 0
            if s[i] == s[j]:
                return lps(i + 1, j - 1) + 2
            else:
                return max(lps(i, j - 1), lps(i + 1, j))

        return lps(0, N - 1)
