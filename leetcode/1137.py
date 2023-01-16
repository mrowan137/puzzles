"""
Runtime: 64 ms, faster than 5.04% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 14.2 MB, less than 45.35% of Python3 online submissions for N-th Tribonacci Number.
"""
# performance optimization
class Trib:
    def __init__(self):
        self.dp = [0, 1, 1] + [0] * 35
        for i in range(3, 38):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] + self.dp[i - 3]


class Solution:
    t = Trib()

    def tribonacci(self, n: int) -> int:
        return self.t.dp[n]


# space optimization
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c, d = 0, 1, 1, 2
        if n < 4:
            return [a, b, c, d][n]
        for i in range(n - 3):
            d, c, b, a = d + c + b, d, c, b

        return d
