"""
Runtime: 20 ms, faster than 99.45% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 45.52% of Python3 online submissions for Reverse Integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        rev, x_orig = 0, x
        INT_MAX = 2 ** 31 - 1
        INT_MIN = 2 ** 31 * -1

        x *= -1 if x_orig < 0 else 1

        while x:
            # pop last digit
            add = x % 10
            x //= 10

            # bounds checking
            if rev * 10 + add > INT_MAX:
                return 0
            if rev * 10 + add < INT_MIN:
                return 0

            # add to the rev
            rev = rev * 10 + add

        rev *= -1 if x_orig < 0 else 1

        return rev
