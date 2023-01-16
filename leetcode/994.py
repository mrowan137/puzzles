"""
Runtime: 88 ms, faster than 13.29% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14.4 MB, less than 37.87% of Python3 online submissions for Rotting Oranges.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid[0]), len(grid)

        # grid with no fresh fruits takes 0 to infect
        if max(max([grid[j][i] for i in range(M)]) for j in range(N)) == 0:
            return 0

        rotten, fresh = [], 0
        for i in range(M):
            for j in range(N):
                if grid[j][i] == 2:
                    rotten.append((i, j))
                elif grid[j][i] == 1:
                    fresh += 1

        t = -1
        while rotten:
            t += 1
            for r in rotten:
                i, j = r
                grid[j][i] = 0

                # infect fresh neighbors
                for d in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
                    dx, dy = d
                    if i + dx < 0 or i + dx >= M or j + dy < 0 or j + dy >= N:
                        continue
                    if grid[j + dy][i + dx] == 1:
                        grid[j + dy][i + dx] = 2
                        fresh -= 1

                # check for rotten fruits
                new = []
                for i in range(M):
                    for j in range(N):
                        if grid[j][i] == 2:
                            new.append((i, j))
                rotten = new

        return t if fresh == 0 else -1
