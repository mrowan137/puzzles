"""
Runtime: 1848 ms, faster than 35.92% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 29.6 MB, less than 26.91% of Python3 online submissions for Best Time to Buy and Sell Stock III.
"""
# O(N) two pass -- optimized from TLE below
# How did we do it?  It rely on an observation: the best buy-sell-by-sell
# cannot have two overlaps, so we can compute the first 0 trade so far buy-sell,
# which is dp0, and using this information compute the dp1 buy sell.  This is
# basically make a dp array of size [[0]*sz for _ in range(2)], and we fill out
# row by row instead of the O(N^2) calculation, which is possible by removing
# redundant calculations() there is much repeated calculations when doing the
# for i in range(1,sz): for j in range(1,i): calculation, note that
# prices[j] + dp0[j-1] does not depend on i in the inner calculation, so we
# compute these same number many times.  it is removed in dp O(2*N) approach.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # max profit given I made 0, 1 transactions so far
        dp0, dp1 = [0] * sz, [0] * sz

        # initial condition
        dp1[0] = float("-inf")

        # options each day is we can buy or sell
        mn = float("inf")
        mx = float("-inf")
        for i in range(1, sz):
            mn = min(prices[i - 1], mn)
            dp0[i] = max(prices[i] - mn, mx)  # buy low sell high  # do nothing
            mx = max(dp0[i], mx)

        mn = float("inf")
        for j in range(1, sz):
            mn = min(mn, prices[j] - dp0[j - 1])
            dp1[j] = max(
                dp1[j], prices[j] - mn  # buy low sell high
            )  # plus the 0 trade max

        return max(dp1 + dp0)


"""
TLE
"""
# O(N^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # max profit given I made 0, 1 transactions so far
        dp0, dp1 = [0] * sz, [0] * sz

        # initial condition
        dp1[0] = float("-inf")

        # options each day is we can buy or sell
        for i in range(1, sz):
            dp0[i] = max(
                prices[i] - min(prices[:i]), max(dp0)  # buy low sell high
            )  # do nothing
            for j in range(1, i):
                dp1[i] = max(
                    dp1[i], prices[i] - prices[j] + dp0[j - 1]
                )  # buy low sell high
                # plus the 0 trade max

        return max(dp1 + dp0)


"""
Runtime: 1260 ms, faster than 53.87% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 27.8 MB, less than 89.80% of Python3 online submissions for Best Time to Buy and Sell Stock III.
"""
# dp O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # dp[k][i] = max profit given k transactions,
        # considering up to ith day, [0:i+1]
        dp = [[0] * sz for _ in range(3)]

        for k in range(1, 3):
            m = float("inf")
            for i in range(sz):
                m = min(m, prices[i] - dp[k - 1][i])
                dp[k][i] = max(
                    dp[k][i - 1],  # no transaction
                    prices[i] - m,  # there was a transaction some day
                )

        return dp[-1][-1]


# Brute force dp, O(N^2) writing fully within nested loops
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # dp[k][i] = max profit given k transactions,
        # considering up to ith day, [0:i+1]
        dp = [[0] * sz for _ in range(3)]

        for k in range(1, 3):
            for i in range(1, sz):
                for j in range(i):
                    dp[k][i] = max(
                        dp[k][i - 1],  # no transaction
                        prices[i]
                        - prices[j]
                        + dp[k - 1][j],  # there was a transaction some day
                        dp[k][i],  # max iterating over k
                    )

        return dp[-1][-1]


# Brute force dp, O(N^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sz = len(prices)

        # dp[k][i] = max profit given k transactions,
        # considering up to ith day, [0:i+1]
        dp = [[0] * sz for _ in range(3)]

        for k in range(1, 3):
            for i in range(sz):
                m = float("inf")
                for j in range(i):
                    m = min(m, prices[j] - dp[k - 1][j])

                dp[k][i] = max(
                    dp[k][i - 1], prices[i] - m  # no transaction
                )  # there was a transaction some day

        return dp[-1][-1]


# Brute force with helper function, O(N^2)
class Solution:
    def maxProfitOne(self, prices):
        if len(prices) < 2:
            return 0
        smallest_seen = float("inf")
        res = 0
        for p in prices:
            smallest_seen = min(smallest_seen, p)
            res = max(res, p - smallest_seen)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            res = max(
                res,
                self.maxProfitOne(prices[:i]),
                self.maxProfitOne(prices[i:]),
                self.maxProfitOne(prices[:i]) + self.maxProfitOne(prices[i:]),
            )
        return res
