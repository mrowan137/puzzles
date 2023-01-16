"""
Runtime: 489 ms, faster than 9.84% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
Memory Usage: 28.3 MB, less than 13.02% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
"""


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sz = len(arr)

        # max ending at idx i, given 0 or 1 deletions so far
        m0, m1 = [float("-inf")] * sz, [float("-inf")] * sz
        for i in range(sz):
            m0[i] = max(
                m0[i - 1] + arr[i], arr[i]  # 0 deletions max so far, plus curr
            )  # or sum is restarted at current
            m1[i] = max(
                m0[i - 1],  # 0 deletions max so far, ignore curr
                m1[i - 1] + arr[i],
            )  # or 1 deletions max so far, plus curr

        return max(m0 + m1)


"""
Runtime: 292 ms, faster than 54.86% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
Memory Usage: 26.2 MB, less than 34.86% of Python3 online submissions for Maximum Subarray Sum with One Deletion.
"""
# dp O(N*2)
from functools import reduce


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # inputs:  array of numbers
        # outputs: subarray such that, subarray\el has max sum of all such subarrays
        # example: [1,-1,3] --> [1, -1, 3] because sum([1, 3]) == 4 is largest sum
        # strategies:
        #   - recursion?
        #       let f(n) :=  maximum subarray considering up to nth element.
        #       can we write a recursive relationship?
        #       f(n) =
        #       * flash of insigh: this will be approachable with dynamic programming
        #   - dynamic programming: we have a constraint, that is we can delete an elem,
        #     and this may be encoded into our dp table, allowing us to write recursive
        #     identity
        #
        #     define dp[j][i] is the max subarray considering up to ith element
        #     and we have deleted j elems.
        #     the choice we have is to include or delete the current element
        #     dp[j][i] = max( dp[j][i-1] + arr[i], # we don't delete an element
        #                     dp[j-1][i-1]         # we delete current elem
        #                    )
        sz = len(arr)

        # dp[j][i] is max subarray up to ith element with j deletions
        dp = [[float("-inf")] * sz for _ in range(2)]

        # initial condition: no empty subarray
        dp[0][0] = arr[0]

        # update rule
        for j in range(2):
            for i in range(1, sz):  # don't overwrite the initial condition
                dp[j][i] = max(
                    dp[j][i - 1] + arr[i],  # add me to current count
                    dp[j - 1][i - 1],  # keep count, remove me
                    arr[i],  # start a new count
                )

        return reduce(lambda x, y: max(max(x), max(y)), dp)
