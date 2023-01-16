"""
Runtime: 59 ms, faster than 8.38% of Python3 online submissions for Integer Break.
Memory Usage: 14.1 MB, less than 91.62% of Python3 online submissions for Integer Break.
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        # consider a number n there are two cases for optimal decompose:
        # 1. n is sum of two numbers         --> (i-j)*(j+1)
        # 2. n is sum of more than 2 numbers --> (i-j)*dp[j]
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] * (i - j), (j + 1) * (i - j))
        return dp[-1]


"""
Runtime: 24 ms, faster than 98.25% of Python3 online submissions for Integer Break.
Memory Usage: 14.2 MB, less than 75.47% of Python3 online submissions for Integer Break.
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] is the max product breaking the sum i into integers
        dp = [0] * (n + 1)

        # i.c.: the sum 3+0 gives a factor sum 0. and 1 = 1 gives 0
        # 2 is the base case gives 2 = 1 + 1 --> 1 product
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            for j in range((i - 1) // 2 + 1, -1, -1):
                # note dp[i] not necessarily < i! e.g. 2, dp[2] = 1.
                # thus when splitting like 4 = 2 + 2, we could choose to split 0, 1, or both 2s.
                # also we can limit the sum to avoid repeats:
                # 4 = 1+3, 2+2 [, 3+1]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]
