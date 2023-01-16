"""
Runtime: 36 ms, faster than 72.14% of Python3 online submissions for Minimum One Bit Operations to Make Integers Zero.
Memory Usage: 14.2 MB, less than 53.57% of Python3 online submissions for Minimum One Bit Operations to Make Integers Zero.
"""
# Time: logn, space: logn; use a memo
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # first know the pattern:
        # 1: 01 --> 00 = 1
        # 2: 10 --> 11 --> 01 + f(1) = 3
        # 4: 100 --> 101 --> 111 --> 110 --> 010 + f(2) = 7
        # 2**k takes 2^(k+1) - 1
        # we want to take a num
        # 1xxxx --> 11000 --> 01000 --> 00000
        #        ?        +1        + 2^(k-1) - 1
        # where k is the smallest 2^k > n.
        # note also f(?) = f(n^11000)
        # because it's same number of steps take 1xxxx --> 11000
        # as takes n^11000 to 0(, e.g. 11000^11000=0)
        dp = {0: 0}

        def f(n):
            if n in dp:
                return dp[n]
            k = 1
            while k <= n:
                k <<= 1
            dp[n] = f(n ^ (k >> 1) ^ (k >> 2)) + (k >> 1)
            return dp[n]

        return f(n)


"""
Runtime: 75 ms, faster than 6.07% of Python3 online submissions for Minimum One Bit Operations to Make Integers Zero.
Memory Usage: 13.8 MB, less than 96.07% of Python3 online submissions for Minimum One Bit Operations to Make Integers Zero.
"""
# Time: logn, space: logn;
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # first know the pattern:
        # 1: 01 --> 00 = 1
        # 2: 10 --> 11 --> 01 + f(1) = 3
        # 4: 100 --> 101 --> 111 --> 110 --> 010 + f(2) = 7
        # 2**k takes 2^(k+1) - 1
        # we want to take a num
        # 1xxxx --> 11000 --> 01000 --> 00000
        #        ?        +1        + 2^(k-1) - 1
        # where k is the smallest 2^k > n.
        # note also f(?) = f(n^11000)
        # because it's same number of steps take 1xxxx --> 11000
        # as takes n^11000 to 0(, e.g. 11000^11000=0)
        if n == 0:
            return 0
        k = 1
        while k <= n:
            k <<= 1
        return (
            self.minimumOneBitOperations(n ^ (k >> 1) ^ (k >> 2))
            + 1
            + (k >> 1)
            - 1
        )
