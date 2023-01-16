"""
Runtime: 64 ms, faster than 51.58% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 64.50% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Insight: [1,2,3,4,5]
        # It doesn't matter if 1, or 4 transations.
        # We can predict the future, so buy and sell only if it goes up
        profit = 0
        for i in range(len(prices) - 1):
            p_today, p_tomorrow = prices[i], prices[i + 1]
            profit += (p_tomorrow - p_today) * (p_tomorrow > p_today)
        return profit


"""
Runtime: 60 ms, faster than 70.42% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 86.81% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            x, y = prices[i], prices[i + 1]
            profit += (y - x) * ((y - x) >= 0)

        return profit
