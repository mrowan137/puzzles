"""
Runtime: 40 ms, faster than 93.44% of Python3 online submissions for Reducing Dishes.
Memory Usage: 14 MB, less than 66.74% of Python3 online submissions for Reducing Dishes.
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # we want to add the tastiest dishes many times as posible
        # but we would take even the untasty dish if it let us add
        # enough tasty
        satisfaction.sort()

        # the final max tasty
        res = 0

        # the partial sum
        partial = 0

        # idx into the tasty
        i = len(satisfaction) - 1

        while i >= 0 and satisfaction[i] + partial > 0:
            partial += satisfaction[i]
            i -= 1
            res += partial

        return res
