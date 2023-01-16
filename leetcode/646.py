"""
Runtime: 2309 ms, faster than 32.63% of Python3 online submissions for Maximum Length of Pair Chain.
Memory Usage: 15 MB, less than 32.54% of Python3 online submissions for Maximum Length of Pair Chain.
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sz = len(pairs)
        dp = [1] * sz
        # dp[i] = 'the longest pair chain, considering up to ith] pair'
        # dp[i] = ?
        # algorithm:
        #     1. iterate through j < i
        #     2. if pairs[j][1] < pairs[i][0]:
        #            dp[i] = max(dp[i], dp[j] + 1)

        # true statement: every pair chain satisfies that the 0th element
        #                 is strictly increasing (otherwise, a pair ending
        #                 could come after a pair beginning).  we sort because
        #                 pairs with earliest start time is potentially at
        #                 the beginning
        pairs = sorted(pairs)
        for i in range(1, sz):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
