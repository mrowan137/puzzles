"""
Runtime: 34 ms (beats 94.41%)
Memory: 13.8 MB (beats 80.6%)
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


"""
TLE
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.recurse(piles)

    def recurse(self, piles):
        if len(piles) == 0:
            return 0
        if len(piles) == 1:
            return 0
        if len(piles) % 2 == 0:
            return max(
                piles[0] + self.stoneGame(piles[1:]),
                piles[-1] + self.stoneGame(piles[:-1]),
            )

        elif len(piles) % 2 == 1:
            return min(
                -piles[0] + self.stoneGame(piles[1:]),
                -piles[-1] + self.stoneGame(piles[:-1]),
            )

        return recurse(piles) > 0
