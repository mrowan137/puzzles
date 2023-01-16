"""
Runtime: 527 ms, faster than 22.22% of Python3 online submissions for Target Sum.
Memory Usage: 14.8 MB, less than 56.75% of Python3 online submissions for Target Sum.

recursion with memo -- O(len(nums)*target)
recursion + memo, sometimes it's easier than a 2d dp
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def _(i, t, m):
            if (i, t) in m:
                return m[(i, t)]
            if i < 0 and t == 0:
                return 1
            if i < 0:
                return 0

            res = 0
            res += _(i - 1, t + nums[i], m) + _(i - 1, t - nums[i], m)

            m[(i, t)] = res
            return res

        memo = {}
        return _(len(nums) - 1, target, memo)
