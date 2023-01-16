"""
Runtime: 736 ms, faster than 50.77% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 21.3 MB, less than 58.59% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
"""
# O(N)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        # dp[i] is the max profit on day i
        dp = [0] * N

        m = float("inf")
        for i in range(1, N):
            # The straight forward way is to compute min of prices[j]-dp[j-1]
            # by iterating over j;
            #
            #     for j in range(i): m = min(m, prices[j] - dp[j-1])
            #
            # but we can make the clever observation
            # that iterating over i, there will be many repeat calculations
            # and we could instead track that min value when iterating over i
            m = min(m, prices[i - 1] - dp[i - 2])
            dp[i] = max(
                dp[i - 1], prices[i] - m - fee  # no transaction ith day
            )  # transaction jth day

        return max(dp)


"""
Runtime: 816 ms, faster than 43.15% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
Memory Usage: 21.3 MB, less than 55.23% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

problem solving hints:
1. solve a simpler problem (relax assumptions)
       - no fee
2. break the problem into pieces
3. rephrase the problem (frame switch)
4. define one or more useful variable and assume it exists, 
   to use induction/dynamic programming/recursion
       - these could cover all possible cases
       - look for a recursive relation
5. generalize the problem
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)

        # definitions
        dp1 = [0] * (N)  # max profit end of day i,
        # given you have 1 stock at the end of the day

        dp0 = [0] * (N)  # max profit end of day i,
        # given you have 0 stock at the end of the day

        # initial conditions
        dp1[-1] = -float("inf")  # max profit at beginning of 0th day, given 1
        # stock at beginning of 0th day is an impossible
        # situation.  this lets
        #   dp0[0] = max(dp0[-1], dp1[-1] + prices[i])
        #          = max(0, -inf)
        #          = 0

        dp0[0] = 0  # max profit at end of 0th day, given 0 stock
        # at end of day is 0; meaning, you start with
        # 0 profit

        # iterate
        for i in range(N):
            dp0[i] = max(
                dp0[i - 1], dp1[i - 1] + prices[i] - fee  # rest  # sell
            )
            dp1[i] = max(dp1[i - 1], dp0[i - 1] - prices[i])  # rest  # buy

        return dp0[-1]
