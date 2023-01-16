"""
Runtime: 32 ms, faster than 69.77% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 96.04% of Python3 online submissions for Unique Paths.

We can also think of the alternate math solution
m-1 spaces across, n-1 spaces down
in other words, we take m+n-2 moves to reach the final box
m-1 of these must be across
n-1 of these must be down
so the number of unique paths is Choose(m+n-2, m-1) = Choose(m+n-2, n-1)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0] * (m + 1) for _ in range(n + 1)]

        # initial condition: there is one way to reach the initial square
        ans[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ans[j][i] = ans[j - 1][i] + ans[j][i - 1]

        return ans[-1][-1]


"""
Runtime: 38 ms, faster than 19.44% of Python3 online submissions for Unique Paths.
Memory Usage: 14.2 MB, less than 86.79% of Python3 online submissions for Unique Paths.
"""
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we will take m + n - 2 steps to reach the bottom right
        # m-1 of them must be to the right, the remainder are down
        return comb(m + n - 2, m - 1)
