"""
Runtime: 40 ms, faster than 68.52% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 14.2 MB, less than 80.38% of Python3 online submissions for Kids With the Greatest Number of Candies.
"""


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        # Normalize so largest element is 0
        m = max(candies)
        normalized = [c - m for c in candies]

        # add extras to each, and they have the most if num is positive
        return [n + extraCandies >= 0 for n in normalized]
