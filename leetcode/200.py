"""
Runtime: 160 ms, faster than 28.58% of Python3 online submissions for Number of Islands.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recursion
        m, n = len(grid[0]), len(grid)

        def explore(i, j):
            # out of bounds?
            valid = 0 <= i and i < m and 0 <= j and j < n
            if not valid:
                return

            # water or visited?
            if grid[j][i] in ["x", "0"]:
                return

            # not out of bounds, mark as visited
            grid[j][i] = "x"

            # explore the surrounding cells
            for c in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                explore(i + c[0], j + c[1])

            return 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[j][i] == "1":
                    res += explore(i, j)

        return res
