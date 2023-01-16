"""
Runtime: 24 ms, faster than 97.69% of Python3 online submissions for Egg Drop With 2 Eggs and N Floors.
Memory Usage: 14.3 MB, less than 45.12% of Python3 online submissions for Egg Drop With 2 Eggs and N Floors.
"""


class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = 0
        while ans * (ans + 1) / 2 < n:
            ans += 1
        return ans
