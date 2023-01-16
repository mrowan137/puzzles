"""
Runtime: 24 ms, faster than 94.44% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.2 MB, less than 80.67% of Python3 online submissions for Pascal's Triangle.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        for _ in range(numRows - 1):
            tmp = []
            curr = [0] + res[-1] + [0]
            for i in range(1, len(curr)):
                a, b = curr[i], curr[i - 1]
                tmp += [a + b]

            res.append(tmp)

        return res
