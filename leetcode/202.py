"""
Runtime: 32 ms, faster than 80.74% of Python3 online submissions for Happy Number.
Memory Usage: 14.2 MB, less than 46.84% of Python3 online submissions for Happy Number.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(m):
            ans = 0
            while m:
                r = m % 10
                m //= 10
                ans += r ** 2

            return ans

        n1, n2 = n, n
        while n1 != 1 and n2 != 1:
            n1 = nxt(n1)
            n2 = nxt(nxt(n2))
            if n1 == n2 and n1 != 1 and n2 != 1:
                return False

        return True
