"""
Runtime: 32 ms, faster than 59.70% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.3 MB, less than 41.30% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda x, y: x * y, [int(j) for j in str(n)]) - sum(
            [int(j) for j in str(n)]
        )
