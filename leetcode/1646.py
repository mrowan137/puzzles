"""
Runtime: 24 ms, faster than 96.48% of Python3 online submissions for Get Maximum in Generated Array.
Memory Usage: 14.3 MB, less than 47.08% of Python3 online submissions for Get Maximum in Generated Array.
"""


class T:
    def __init__(self):
        res = [0, 1] + [0] * 98
        for i in range(2, 100):
            if i % 2 == 0:
                res[i] = res[i // 2]
            elif i % 2 == 1:
                res[i] = res[i // 2] + res[i // 2 + 1]

        self.res = res


t = T()


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        return max(t.res[0 : n + 1])
