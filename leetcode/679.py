"""
Runtime: 136 ms, faster than 57.04% of Python3 online submissions for 24 Game.
Memory Usage: 13.9 MB, less than 93.47% of Python3 online submissions for 24 Game.
"""


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return self.dfs(cards)

    def dfs(self, nums):
        # base case: are we close to 24?
        if len(nums) == 1:
            return abs(24 - nums[0]) < 0.01

        # iterate through all possible pairs in the list (nums[i], nums[j])
        # and all possible ways to operate those pairs together
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # we form a new list: [combined, and the rest]
                for combo in self.combos(nums[i], nums[j]):
                    theRest = [
                        nums[k] for k in range(len(nums)) if k != i and k != j
                    ]
                    nextRound = [combo] + theRest

                    # if it ever reduced to 24, we're done
                    if self.dfs(nextRound):
                        return True

        # if we never came upon a magical 24, we lose
        return False

    def combos(self, x, y):
        res = [x + y, x - y, y - x, x * y]
        if y != 0:
            res += [x / y]
        if x != 0:
            res += [y / x]
        return res
