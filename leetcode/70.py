"""
Runtime: 24 ms, faster than 94.49% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.4 MB, less than 12.04% of Python3 online submissions for Climbing Stairs.
"""


class stairs:
    def __init__(self, n):
        dp = [1, 1] + [0] * (n - 2)
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        self.dp = dp


class Solution:
    def __init__(self):
        self.s = stairs(46)

    def climbStairs(self, n: int) -> int:
        return self.s.dp[n]


"""
Runtime: 32 ms, faster than 47.40% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.1 MB, less than 71.47% of Python3 online submissions for Climbing Stairs.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # slow, don't do this
        # if n == 0 or n == 1: return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n == 0 or n == 1:
            return 1
        a, b = 1, 1
        while n - 1:
            a, b = a + b, a
            n -= 1

        return a
