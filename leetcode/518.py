"""
Runtime: 338 ms, faster than 41.55% of Python3 online submissions for Coin Change 2.
Memory Usage: 14.6 MB, less than 50.57% of Python3 online submissions for Coin Change 2.
"""
# dp O(amount*len(coins))
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] is the number of ways to form amount i
        dp = [0] * (amount + 1)

        # there's one ways to form the amount 0: it's just, 0
        dp[0] = 1

        # note again how the order of the loops was crucial.
        # if we reversed it, we would overcount, because
        # we would get
        # coins = [1,2,3], amount = 4
        # dp[2] = 1+1
        # dp[3] = 1+1+1 = 1+2 --> 2
        # dp[4] = 1+1+2 = 1+1+1+1 = 1+2+1 --> 3 (overcounter 1+2+1, 1+1+2 twice)
        # so the solution is compute ways to reach sums using sequence of 1,
        # then sequence of 1...1 2...2, then sequence of 1...1 2...2 3...3
        for c in coins:
            for i in range(1, amount + 1):
                # the number of ways to form amount i is number of ways
                # to form partial sum of i-c, and add 1 for the new coin
                if i - c >= 0:
                    dp[i] += dp[i - c]

        return dp[-1]


"""
Runtime: 240 ms, faster than 56.97% of Python3 online submissions for Coin Change 2.
Memory Usage: 14.5 MB, less than 51.73% of Python3 online submissions for Coin Change 2.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] represents the number of combos to reach i coins
        dp = [0] * (amount + 1)
        dp[0] = 1

        # It is crucial to do in this order.
        # if reverse the loops and follow nose, overcount 1+2 = 2+1 = 3.
        # we compute the number of ways to reach each amount first using only 1s.
        # then knowing how to reach each spot usings 1s find num ways to reach spots using 2s (and 1s).
        # then knowing spots reachable in a sequence of 1s and 2s find num ways to reach using 5s (and 2s and 1s).
        for c in coins:
            for i in range(1, amount + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]

        return dp[-1]
