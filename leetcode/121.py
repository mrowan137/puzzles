"""
Runtime: 1096 ms, faster than 43.98% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 81.86% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# O(N) time O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float("inf")
        for i in range(1, len(prices)):
            min_so_far = min(min_so_far, prices[i - 1])
            max_profit = max(max_profit, prices[i] - min_so_far)

        return max_profit


"""
Runtime: 1172 ms, faster than 20.22% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 11.08% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
# O(N) time and space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # dp[i] = max profit on day i
        dp = [0] * sz

        min_so_far = float("inf")
        for i in range(1, sz):
            min_so_far = min(min_so_far, prices[i - 1])
            dp[i] = max(
                dp[i - 1],  # if I take no action
                prices[i] - min_so_far,  # if I sell
            )

        return dp[-1]


"""
Runtime: 1413 ms, faster than 15.22% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 95.35% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -float("inf")
        pmin = float("inf")
        for p in prices:
            pmin = min(pmin, p)
            profit = max(profit, p - pmin)

        return profit


"""
Runtime: 1096 ms, faster than 39.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pmin = float("inf")
        res = -float("inf")
        for p in prices:
            pmin = min(p, pmin)
            res = max(res, p - pmin)

        return res
