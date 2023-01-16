"""
Runtime: 37 ms, faster than 43.28% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.9 MB, less than 88.59% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""
# bit
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # binary is like 0000101001
        #                xxxxssssss
        # the answer will be num of s - 1 (for divides)
        # and we need to add how many those are 1s
        res = -1
        while num:
            res += (num & 0x00000001) + 1
            num >>= 1
        return max(res, 0)


"""
Runtime: 24 ms, faster than 95.97% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 14.2 MB, less than 68.74% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            res += 1

        return res
