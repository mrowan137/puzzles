"""
Runtime: 387 ms, faster than 5.68% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.3 MB, less than 32.49% of Python3 online submissions for Multiply Strings.
"""
# one liner
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sz1, sz2 = len(num1), len(num2)
        return str(
            sum(
                10 ** (i + j) * int(num1[sz1 - 1 - i]) * int(num2[sz2 - 1 - j])
                for i in range(sz1)
                for j in range(sz2)
            )
        )


"""
Runtime: 340 ms, faster than 7.93% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.3 MB, less than 32.49% of Python3 online submissions for Multiply Strings.
"""
# O(N^2), easy
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # ab*cd = (10*a + b)*(10*c + d)
        res, j = 0, 0
        sz1, sz2 = len(num1), len(num2)
        while j < sz2:
            for i in range(len(num1)):
                res += (
                    10 ** (i + j)
                    * int(num1[sz1 - 1 - i])
                    * int(num2[sz2 - 1 - j])
                )
            j += 1

        return str(res)


"""
Runtime: 168 ms, faster than 26.02% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.2 MB, less than 60.83% of Python3 online submissions for Multiply Strings.
"""
# O(N^2), but more 'to the point' calculation
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if len(num2) > len(num1): return self.multiply(num2, num1)
        num1 = [int(c) for c in num1]  # the longer
        num2 = [int(c) for c in num2]  # the shorter
        sz1, sz2 = len(num1), len(num2)

        # multiply it out
        res = 0
        carry = 0
        for i in range(len(num2) - 1, -1, -1):  # n u m 1
            for j in range(len(num1) - 1, -1, -1):  # n u m 2
                place = (
                    sz1 + sz2 - 2 - i - j
                )  # place where add curr pair product
                res += num1[j] * num2[i] * 10 ** place  # to the next iteration

        return str(res)


"""
Runtime: 288 ms, faster than 7.43% of Python3 online submissions for Multiply Strings.
Memory Usage: 14.1 MB, less than 83.23% of Python3 online submissions for Multiply Strings.
"""
# O(N^2)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if len(num2) > len(num1): return self.multiply(num2, num1)
        num1 = [int(c) for c in num1]  # the longer
        num2 = [int(c) for c in num2]  # the shorter
        sz1, sz2 = len(num1), len(num2)

        # multiply it out
        res = 0
        carry = 0
        for i in range(len(num2) - 1, -1, -1):  # n u m 1
            for j in range(len(num1) - 1, -1, -1):  # n u m 2
                place = (
                    -i - j + sz1 + sz2 - 2
                )  # place to which adding current pair product
                res += carry
                carry, add = divmod(num1[j] * num2[i], 10)
                carry = carry * 10 ** (
                    place + 1
                )  # +1 relative to res b.c. adds
                res += add * 10 ** (place)  # to the next iteration

        return str(res + carry)
