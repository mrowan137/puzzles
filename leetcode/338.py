"""
Runtime: 136 ms, faster than 29.10% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 71.26% of Python3 online submissions for Counting Bits.
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            cnt, m = 0, i + 1
            while m:
                m = m & (m - 1)
                cnt += 1

            res += [cnt]

        return res


"""
Runtime: 112 ms, faster than 38.28% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 91.23% of Python3 online submissions for Counting Bits.
"""
from collections import defaultdict


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        dp = defaultdict(int)
        for i in range(n):
            # count number of bit cancellations
            cnt, m = 0, i + 1
            while m:
                if m in dp.keys():
                    cnt += dp[m]
                    dp[i + 1] += dp[m]
                    break
                m = m & (m - 1)
                dp[i + 1] += 1
                cnt += 1

            res += [cnt]

        return res


"""
Runtime: 68 ms, faster than 99.02% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 91.29% of Python3 online submissions for Counting Bits.
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Look for a pattern
        # 1: 001 --> 1
        # 2: 010 --> 1
        # 3: 011 --> 2
        # 4: 100 --> 1
        # 5: 101 --> 2
        # 6: 110 --> 2
        # 7: 111 --> 3
        # Two cases: least significant bit (LSB) is 1 or 0
        # case 1): LSB == 1
        #   --> res[i] = res[i >> 1] + 1
        # case 2): LSB == 0
        #   We computed all smaller numbers, bit shift i
        #   and then num bits in i is same is i >> 1
        #   --> res[i] = res[i >> 1]

        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + ((i & 1) != 0)
            # expanded:
            # if ((i & 1) == 0):
            #     res[i] = res[i >> 1]
            # else:
            #     res[i] = res[i >> 1] + 1

        return res
