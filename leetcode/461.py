"""
Runtime: 32 ms, faster than 62.28% of Python3 online submissions for Hamming Distance.
Memory Usage: 14.2 MB, less than 72.54% of Python3 online submissions for Hamming Distance.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(d) for d in list("{0:b}".format(x ^ y)))
