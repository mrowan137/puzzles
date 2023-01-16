"""
Runtime: 376 ms, faster than 47.18% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 14.5 MB, less than 74.72% of Python3 online submissions for Sort Integers by The Power Value.
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}  # record power of an integer

        def power(x):
            # return power of an integer
            x_orig = x
            res = 0
            while x != 1:
                if x in dp:
                    res += dp[x]
                    break

                if x % 2 == 0:
                    x = x / 2
                elif x % 2 == 1:
                    x = 3 * x + 1

                res += 1

            dp[x_orig] = res
            return res

        powers = [0 for _ in range(lo, hi + 1)]
        nums = [i for i in range(lo, hi + 1)]
        for i, n in enumerate(nums):
            powers[i] = power(n)

        return sorted(nums, key=lambda i: dp[i])[k - 1]
