"""
Runtime: 1081 ms, faster than 28.77% of Python3 online submissions for Bomb Enemy.
Memory Usage: 21.1 MB, less than 38.13% of Python3 online submissions for Bomb Enemy.
"""
# O(MN)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # idea to iterate cumulative sum along one direction
        # then backtrack taking pairwise max along opposite
        # and do this for vertical and horizontal
        m, n = len(grid[0]), len(grid)
        dph = [[0] * m for _ in range(n)]
        dpv = [[0] * m for _ in range(n)]

        for j in range(n):
            dph[j][0] = int(grid[j][0] == "E")
            for i in range(1, m):
                # cumulative sum
                if grid[j][i] == "W":
                    # hit a wall, reset the count
                    dph[j][i] = 0
                else:
                    # hit a blank or an enemy, update accordingly
                    dph[j][i] = dph[j][i - 1] + int(grid[j][i] == "E")

            for i in range(m - 2, -1, -1):
                if grid[j][i] != "W":
                    dph[j][i] = max(dph[j][i], dph[j][i + 1])

        for i in range(m):
            dpv[0][i] = int(grid[0][i] == "E")
            for j in range(1, n):
                # cumulative sum
                if grid[j][i] == "W":
                    # hit a wall, reset the count
                    dpv[j][i] = 0
                else:
                    # hit a blank or an enemy, update accordingly
                    dpv[j][i] = dpv[j - 1][i] + int(grid[j][i] == "E")

            for j in range(n - 2, -1, -1):
                if grid[j][i] != "W":
                    dpv[j][i] = max(dpv[j][i], dpv[j + 1][i])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[j][i] != "E":
                    # a bomb can't go on the enemy, it is inhumane
                    res = max(res, dph[j][i] + dpv[j][i])

        return res
