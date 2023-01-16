"""
Runtime: 28 ms, faster than 81.72% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14.4 MB, less than 29.63% of Python3 online submissions for Spiral Matrix.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # search the grid
        compass_to_ij = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

        def helper(i, j, c, mat):
            # Exit conditions: oob, visited
            if i < 0 or i >= len(mat[0]) or j < 0 or j >= len(mat):
                return []
            if mat[j][i] == None:
                return []

            # mark visited location
            tmp = matrix[j][i]
            mat[j][i] = None

            # toggle direction if needed
            i_nxt, j_nxt = i + compass_to_ij[c][0], j + compass_to_ij[c][1]
            oob = (
                i_nxt < 0
                or i_nxt >= len(mat[0])
                or j_nxt < 0
                or j_nxt >= len(mat)
            )

            if oob or not matrix[j_nxt][i_nxt]:
                c = (c + 1) % 4
                i_nxt, j_nxt = i + compass_to_ij[c][0], j + compass_to_ij[c][1]

            return [tmp] + helper(i_nxt, j_nxt, c, mat)

        return helper(0, 0, 0, matrix)
