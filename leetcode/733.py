"""
Runtime: 72 ms, faster than 87.87% of Python3 online submissions for Flood Fill.
Memory Usage: 14.6 MB, less than 24.96% of Python3 online submissions for Flood Fill.
"""


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:

        M, N = len(image[0]), len(image)
        oldColor = image[sr][sc]
        seen = set()

        def recurse(i, j):
            # Globals: image, M, N
            if i < 0 or j < 0 or i >= M or j >= N:
                return

            # flood fill if we're in a valid cell
            if image[j][i] == oldColor and (i, j) not in seen:
                seen.add((i, j))
                image[j][i] = newColor

                recurse(i + 1, j)
                recurse(i - 1, j)
                recurse(i, j + 1)
                recurse(i, j - 1)

            return

        recurse(sc, sr)

        return image
