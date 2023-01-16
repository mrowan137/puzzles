"""
Runtime: 188 ms, faster than 97.51% of Python3 online submissions for Maximal Square.
Memory Usage: 15.4 MB, less than 97.88% of Python3 online submissions for Maximal Square.
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix[0]), len(matrix)

        # side length of the square
        s = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # I am a square of sidelength s+1
                # 1) if I am surrounded N, NW, W by square of length s, and
                # 2) if my matrix value is equal to 1
                s[j][i] = (
                    min(s[j - 1][i], s[j][i - 1], s[j - 1][i - 1]) + 1
                ) * (matrix[j - 1][i - 1] == "1")

        return max([max(row) for row in s]) ** 2
