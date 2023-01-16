"""
Runtime: 64 ms, faster than 5.18% of Python3 online submissions for Power of Four.
Memory Usage: 14.3 MB, less than 42.50% of Python3 online submissions for Power of Four.
"""
# O(1) bit magic, more ideas about the calculate
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n is the power of 2, the single 1: 0001
        #                                    0010
        #                                    0100
        # but n is not those ones with the odd idx
        #                                    0001
        #                                    0100
        # power of 2:   00000100000 = n
        #               00000011111 = n-1
        #               11111011111 = ~n
        # n^(n-1) == 2n-1? ~n & n-1 == n-1?
        # it's a power of 2, but not with the 1 at the odd idx
        return n ^ (n - 1) == 2 * n - 1 and 0x55555555 & n == n and n > 0
        # return ~n & n-1 == n-1 and 0x55555555 & n == n and n > 0


"""
Runtime: 28 ms, faster than 87.85% of Python3 online submissions for Power of Four.
Memory Usage: 14.3 MB, less than 42.06% of Python3 online submissions for Power of Four.
"""
# O(1), bit magic
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n must be a power of 2   : n>0 and n & (n-1) == 0
        # n must be of form 2^(2m) : 00000100
        #                            00010000
        #                            01000000
        #                            ...
        # In other words, no bits in odd digits
        # so for n a 32 bit integer,
        # n & (...01010101010) == 0
        #     = 0xaaaaaaaa
        return n > 0 and n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


"""
Runtime: 24 ms, faster than 96.94% of Python3 online submissions for Power of Four.
Memory Usage: 14.3 MB, less than 42.06% of Python3 online submissions for Power of Four.
"""
# O(1), math approach
from math import log2


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n = 4^x = 2^(2x)
        # log2(n)  = 2x --> x = 0.5 log2(n) i an integer
        #               --> log2(n) is even
        return n > 0 and log2(n) % 2 == 0


"""
Runtime: 32 ms, faster than 67.03% of Python3 online submissions for Power of Four.
Memory Usage: 14.3 MB, less than 6.41% of Python3 online submissions for Power of Four.
"""
# O(N), bit manip
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1   0001
        # 4   0100
        # 16 10000
        # Requirements: have only single 1, and even number of leading zeros
        #               equivalently, ~n is an even number of 1s
        n = ~n
        while n:
            if n == -1:
                return False  # n == 0
            if n == -2:
                return True  # ...0001
            if not (n & 3) == 3:
                return False  # not like 11..1111
            n >>= 2  # 2 leading digits check out
