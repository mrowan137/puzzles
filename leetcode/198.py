"""
Runtime: 28 ms, faster than 86.25% of Python3 online submissions for House Robber.
Memory Usage: 14.4 MB, less than 19.79% of Python3 online submissions for House Robber.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        sz = len(nums)
        dp = [0] * sz + [0] * 2
        for i in range(sz):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return max(dp)


"""
Runtime: 48 ms, faster than 13.32% of Python3 online submissions for House Robber.
Memory Usage: 14.2 MB, less than 51.72% of Python3 online submissions for House Robber.
"""
# dp general advice: condition dp on the possible choices
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        # let dp[N] represent the money you earn
        # robbing at most N houses
        dp = [0] * (N + 1)

        # The recursive step, how to compute dp[i]?
        # Robbing patterns:
        #  x    o   x  OR   o    x   o
        # i-2  i-1  i      i-2  i-1  i
        # dp[i] ?= dp[i-1]
        # dp[i] ?= dp[i-2] + nums[i-1]
        # take the max

        # setup
        dp[0], dp[1] = 0, nums[0]
        dp[1] = nums[0]

        # inductive step
        for i in range(2, N + 1):
            # this would be wrong! assumes you rob the ith house.
            #     dp[i] = nums[i-1] + max(dp[i-2], dp[i-3])
            # note the branching choice, rob or don't rob ith house.

            # but this is the right way
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])

        return dp[N]
