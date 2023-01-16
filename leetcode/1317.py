"""
Runtime: 71 ms, faster than 5.08% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
Memory Usage: 13.9 MB, less than 85.88% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
"""
# Silly brute force
class Solution:
    def nozeros(self, n):
        while n:
            n, rem = divmod(n, 10)
            if rem == 0:
                return False

        return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n // 2 + 1):
            if self.nozeros(a):
                if self.nozeros(n - a):
                    return [a, n - a]
