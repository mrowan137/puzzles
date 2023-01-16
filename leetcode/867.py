"""
Runtime: 172 ms, faster than 5.02% of Python3 online submissions for Transpose Matrix.
Memory Usage: 15 MB, less than 13.11% of Python3 online submissions for Transpose Matrix.

How does linear index of element change after transpose?
(N, M = 4, 3)

  0  1  2       0  3  6   9
  3  4  5  -->  1  4  7  10
  6  7  8       2  5  8  11
  9  10 11

look for a pattern?

A:    0   1    2    3    4       5     6    7     8    9    10    11
T(A): 0   3    6    9    1       4     7    10    2    5     8    11
          1*3  2*3  3*3  4*3%11  5*3%11 ..
        
conjecture: i_new = (i * N) % (N * M - 1)
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        N, M = len(matrix), len(matrix[0])
        sz = N * M

        # fill transpose with the original order
        transpose = [0] * sz
        for i in range(sz):
            transpose[i] = matrix[i // M][i % M]

        # first and last elements stay where they are
        placed = [0] * sz
        placed[0] = 1
        placed[-1] = 1

        # move elements in independent cycles;
        # find the next needs replacement
        begin = 1

        while begin < sz and any([p == 0 for p in placed]):
            i = begin
            curr = transpose[i]
            while True:
                i = (i * N) % (M * N - 1)
                curr, transpose[i] = transpose[i], curr
                placed[i] = 1
                if i == begin:
                    break

            # find the new begin spot
            begin = 1
            while begin < sz and placed[begin]:
                begin += 1

        # fill in the final transpose matrix
        ret = [[0] * N for _ in range(M)]
        for idx in range(sz):
            ret[idx // N][idx % N] = transpose[idx]

        return ret
