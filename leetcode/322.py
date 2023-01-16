"""
Runtime: 1460 ms, faster than 59.65% of Python3 online submissions for Coin Change.
Memory Usage: 14.5 MB, less than 80.25% of Python3 online submissions for Coin Change.
"""
# dp cleanup -- O(amount*len(coins))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] the minimum number of coins to reach amount
        dp = [float("inf")] * (1 + amount)

        # it takes 0 coins to reach 0 money
        dp[0] = 0

        for target in range(1, amount + 1):
            # target is amount we want to reach
            for c in coins:
                # difference is the amount to form with a coins
                if target - c >= 0:
                    dp[target] = min(dp[target], dp[target - c] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1


"""
Runtime: 6196 ms, faster than 5.01% of Python3 online submissions for Coin Change.
Memory Usage: 14.5 MB, less than 80.25% of Python3 online submissions for Coin Change.
"""
# dp O(amount*len(coins)*amount/min(coins)) ~O(N^2*M)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin = sorted(coins)[::-1]

        # dp[i] the minimum number of coins to reach amount
        dp = [float("inf")] * (1 + amount)

        # it takes 0 coins to reach 0 money
        dp[0] = 0

        for target in range(1, amount + 1):
            # target is amount we want to reach
            for c in coins:
                # difference is the amount to form with a coins
                n = 1
                while target - n * c >= 0:
                    # this works, but notice how we overcalculate
                    # we only need to look at the n=1 case because
                    # dp[i] =  dp[i - c]          + 1
                    #       = (dp[i - c - c] + 1) + 1
                    #       = (dp[i - 2c]         + 2
                    # so there would be redundant calculations b/c
                    # dp[i-1*c] + 1 == dp[i-n*c] + n, there is no lower
                    difference = target - n * c
                    dp[n * c] = min(dp[n * c], n)
                    if dp[n * c] != float("inf"):
                        dp[target] = min(dp[target], dp[target - n * c] + n)
                        break

                    n += 1

        return dp[-1] if dp[-1] != float("inf") else -1


"""
TLE
"""
# recursion with the memo
from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = sorted(coins)[::-1]

        def dfs(a, memo):
            if a in memo.keys():
                return memo[a]
            res = float("inf")
            for c in coins:
                n = 1
                while a - n * c >= 0:
                    if dfs(a - n * c, memo) != float("inf"):
                        res = min(res, dfs(a - n * c, memo) + n)
                        break
                    memo[n * c] = min(memo[n * c], n)
                    n += 1

            memo[a] = res
            return res

        memo = defaultdict(lambda: float("inf"))
        memo[0] = 0
        res = dfs(amount, memo)
        return res if res != float("inf") else -1


"""
TLE
"""
# naive dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin = sorted(coins)[::-1]

        # dp[i] the minimum number of coins to reach amount
        dp = [float("inf")] * (1 + amount)

        # it takes 0 coins to reach 0 money
        dp[0] = 0

        for target in range(1, amount + 1):
            # target is amount we want to reach
            for c in coins:
                # difference is the amount to form with a coins
                for partial in range(target - 1, -1, -1):
                    difference = target - partial
                    if difference % c == 0:
                        dp[target] = min(
                            dp[target], dp[partial] + difference // c
                        )
                        break

        return dp[-1] if dp[-1] != float("inf") else -1


"""
Runtime: 1440 ms, faster than 64.21% of Python3 online submissions for Coin Change.
Memory Usage: 14.3 MB, less than 92.01% of Python3 online submissions for Coin Change.
"""
# dp -- O(N)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] is the fewest number of coins needed to reach i
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
