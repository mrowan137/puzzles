"""
Runtime: 607 ms, faster than 36.01% of Python3 online submissions for Longest Line of Consecutive One in Matrix.
Memory Usage: 18.7 MB, less than 32.17% of Python3 online submissions for Longest Line of Consecutive One in Matrix.
"""


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        M, N = len(mat[0]), len(mat)

        dph = [[0] * M for _ in range(N)]
        dpv = [[0] * M for _ in range(N)]
        dpd = [[0] * M for _ in range(N)]
        dpad = [[0] * M for _ in range(N)]

        # initial condition
        for j in range(N):
            dph[j][0] = mat[j][0]
        for i in range(M):
            dpv[0][i] = mat[0][i]

        for j in range(N):
            dpd[j][0] = mat[j][0]
        for i in range(1, M):
            dpd[0][i] = mat[0][i]
        for j in range(N):
            dpad[j][0] = mat[j][0]
        for i in range(M - 1):
            dpad[0][i] = mat[0][i]

        for i in range(1, M):
            for j in range(N):
                dph[j][i] = int(mat[j][i] == 1) * (1 + dph[j][i - 1])

        for j in range(1, N):
            for i in range(M):
                dpv[j][i] = int(mat[j][i] == 1) * (1 + dpv[j - 1][i])

        for j in range(1, N):
            for i in range(1, M):
                dpd[j][i] = int(mat[j][i] == 1) * (1 + dpd[j - 1][i - 1])

        for j in range(N - 2, -1, -1):
            for i in range(1, M):
                dpad[j][i] = int(mat[j][i] == 1) * (1 + dpad[j + 1][i - 1])

        m_h = max(max(row) for row in dph)
        m_v = max(max(row) for row in dpv)
        m_d = max(max(row) for row in dpd)
        m_ad = max(max(row) for row in dpad)

        return max(m_h, m_v, m_d, m_ad)
