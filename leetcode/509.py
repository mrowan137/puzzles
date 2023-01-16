"""
Runtime: 28 ms, faster than 84.60% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 98.07% of Python3 online submissions for Fibonacci Number.
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b

        return a
