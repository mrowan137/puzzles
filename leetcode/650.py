"""
Runtime: 34 ms, faster than 74.46% of Python3 online submissions for 2 Keys Keyboard.
Memory Usage: 14 MB, less than 99.18% of Python3 online submissions for 2 Keys Keyboard.

1  =         --> 0
2  = c p     --> 2
3  = c p p   --> 3
4  = c p p p --> 4
   = c p c p --> 4
6  = c p p c p --> 5
   = c p p p p p --> 5
7  = c p p p p p p --> 7
8  = c p c p c p --> 6       = 2*2*2 = f(2)*f(2)*f(2)
   = c p c p p p --> 6       = 
9  = c p p p p p p p p --> 9 = 1*9 = 
9  = c p p c p p --> 6       = 3*3 = f(3)*f(3)
10 = c p c p p p p -->       = 2*5 = f(2)*f(5) 
f(n) = sum of prime factors of n
"""


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        def prime_factors(n):
            res = []
            i = 2
            while i * i <= n:
                while n % i == 0:
                    res.append(i)
                    n //= i
                i += 1
            if n > 1:
                res.append(n)
            return res

        return sum(prime_factors(n))
