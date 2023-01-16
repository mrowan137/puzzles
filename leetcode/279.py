"""
Runtime: 456 ms, faster than 75.46% of Python3 online submissions for Perfect Squares.
Memory Usage: 14.5 MB, less than 55.72% of Python3 online submissions for Perfect Squares.
"""
# dp -- do some compute beforehands
class numSquares:
    def __init__(self, n):
        # dp[i] is the min number of square need to reach the i
        dp = [0] + [float("inf")] * n

        # generate the nums up to n
        for i in range(1, n + 1):
            # for each i, test all the perfect squares can add to it
            x = 1

            # as long as 0 < x < sqrt(i)
            while x ** 2 <= i and x > 0:
                dp[i] = min(dp[i], dp[i - x ** 2] + 1)
                x += 1

        self.dp = dp

    def __call__(self, n):
        return self.dp[n]


ans = numSquares(10 ** 4 + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return ans.dp[n]


"""
TLE
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # target, sqrt(num) to consider, partial sum, how many in partial sum
        todo = [[n, 1, 0, 0]]
        res = float("inf")
        while todo:
            target, i, partial, num_partials = todo.pop()
            m = target // i ** 2
            while m * i ** 2 >= 0 and i ** 2 <= target:
                if m * i ** 2 == target:
                    res = min(res, num_partials + m)
                elif num_partials + m < res:
                    todo.append(
                        [
                            target - m * i ** 2,
                            i + 1,
                            partial + m * i ** 2,
                            num_partials + m,
                        ]
                    )

                m -= 1

        return res


"""
Runtime: 284 ms, faster than 80.76% of Python3 online submissions for Perfect Squares.
Memory Usage: 14.3 MB, less than 70.91% of Python3 online submissions for Perfect Squares.
"""
from math import sqrt


class NumSquares:
    def __init__(self, n):
        # dp[i] is min number of square numbers that sum to i
        dp = [float("inf")] * (n + 1)

        # i.c.
        dp[0] = 0
        dp[1] = 1

        # check the square nums in [1, 2, ..., sqrt(i)]
        # e.g. 100: j^2=1 and numways(99)
        #           j^2=4 and numways(96)
        #           j^2=9 and numways(91), ...
        # and we'd stop at j^2 = 100 because we got to numways(0).
        # so the basic recursion rule is:
        # min numbers of ways to reach i with squares is subtract valid squares,
        # and it's 1 + numways to reach that spot at i - j^2.  and take min over all these.
        for i in range(2, n + 1):
            for j in range(int(sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])  # note i-j**2 >= 0

        self.dp = dp


numsquares = NumSquares(10 ** 4 + 1)


class Solution:
    def numSquares(self, n: int) -> int:
        return numsquares.dp[n]
