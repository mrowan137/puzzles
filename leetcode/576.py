"""
Runtime: 126 ms, faster than 77.48% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 16.4 MB, less than 63.36% of Python3 online submissions for Out of Boundary Paths.
"""
# recursion with memo
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def search(i, j, mm, memo):
            if (i, j, mm) in memo:
                return memo[(i, j, mm)]
            # base case: no moves left, and we're out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if mm == 0:
                return int(i < 0 or i >= m or j < 0 or j >= n)
            neighbors = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
            res = 0
            for nb in neighbors:
                res += search(nb[0], nb[1], mm - 1, memo)

            memo[(i, j, mm)] = res

            return res

        memo = {}
        return search(startRow, startColumn, maxMove, memo) % (10 ** 9 + 7)


"""
TLE
"""
# Brute force -- naive recursion
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def search(i, j, mm):
            # base case: no moves left, and we're out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if mm == 0:
                return int(i < 0 or i >= m or j < 0 or j >= n)
            neighbors = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
            res = 0
            for nb in neighbors:
                res += search(nb[0], nb[1], mm - 1)
            return res

        return search(startRow, startColumn, maxMove)
