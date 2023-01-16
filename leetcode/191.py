"""
Runtime: 32 ms, faster than 56.83% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 14.4 MB, less than 5.13% of Python3 online submissions for Number of 1 Bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1

        return res


"""
Runtime: 36 ms, faster than 30.08% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 14.1 MB, less than 66.43% of Python3 online submissions for Number of 1 Bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n = n & (n - 1)
            cnt += 1

        return cnt
