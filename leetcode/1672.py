"""
Runtime: 44 ms, faster than 98.19% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14.4 MB, less than 29.91% of Python3 online submissions for Richest Customer Wealth.
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(r) for r in accounts])
