"""
Runtime: 548 ms, faster than 38.06% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22 MB, less than 81.47% of Python3 online submissions for Longest Common Subsequence.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sz1, sz2 = len(text1), len(text2)

        # dp[j][i] i the longest common subsequence considering
        # up to idx j in text2 and idx i in text1
        dp = [[0] * (1 + sz1) for _ in range(1 + sz2)]

        for j in range(1, sz2 + 1):
            for i in range(1, sz1 + 1):
                dp[j][i] = max(
                    dp[j - 1][i],
                    dp[j][i - 1],
                    int(text2[j - 1] == text1[i - 1]) + dp[j - 1][i - 1],
                )

        return dp[-1][-1]


"""
Runtime: 392 ms, faster than 84.66% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22.1 MB, less than 70.27% of Python3 online submissions for Longest Common Subsequence.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        # dp[j][i] is the number of matches considering strings end at j, i
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])

        return dp[-1][-1]
