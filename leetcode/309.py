"""
Runtime: 36 ms, faster than 90.52% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 14.5 MB, less than 86.69% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)
        dp = [0] * sz

        m = float("inf")
        for i in range(1, sz):
            # if we transact today, the earliest
            # possible prev transaction ended 3 days
            # ago:      (i-3) (i-2) (i-1) (i-0)
            # ILLEGAL!   buy   sell  buy   sell
            #            sell  cool  buy   sell
            m = min(m, prices[i - 1] - dp[i - 3])
            dp[i] = max(dp[i - 1], prices[i] - m)  # no transaction

        return max(dp)


"""
Runtime: 40 ms, faster than 73.86% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 14.7 MB, less than 24.26% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        # definitions
        dp0 = [0] * (
            N + 2
        )  # max profit at end of ith day given end with 0 stock
        dp1 = [0] * (
            N + 2
        )  # max profit at end of ith day given end with 1 stock

        # initialization
        dp0[
            0
        ] = 0  # start first day with 0 given you 'end' the previous day with 0
        dp1[0] = -float("inf")
        dp1[1] = -float("inf")  # impossible to start 0th day with a stock

        # iterate
        for i in range(2, N + 2):
            dp0[i] = max(dp0[i - 1], dp1[i - 1] + prices[i - 2])  # hold  # sell
            dp1[i] = max(
                dp1[i - 1],  # hold
                dp0[i - 2] - prices[i - 2],  # buy -- but must way a day to buy
            )

        return dp0[-1]
