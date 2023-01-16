"""
Runtime: 1962 ms, faster than 7.94% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
Memory Usage: 18.8 MB, less than 46.43% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        sz1, sz2 = len(s1), len(s2)
        dp = [[0] * (sz1 + 1) for _ in range(sz2 + 1)]

        # IC
        dp[0][0] = 0  # the empty strings match
        for i in range(1, sz1 + 1):
            dp[0][i] = dp[0][i - 1] + ord(s1[i - 1])
        for j in range(1, sz2 + 1):
            dp[j][0] = dp[j - 1][0] + ord(s2[j - 1])

        for j in range(1, sz2 + 1):
            for i in range(1, sz1 + 1):
                # choices: match, delete ith, delete jth
                if s1[i - 1] == s2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(
                        dp[j][i - 1] + ord(s1[i - 1]),
                        dp[j - 1][i] + ord(s2[j - 1]),
                        dp[j - 1][i - 1] + ord(s1[i - 1]) + ord(s2[j - 1]),
                    )

        return dp[-1][-1]
