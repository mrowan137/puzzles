"""
Runtime: 100 ms, faster than 89.68% of Python3 online submissions for Matrix Block Sum.
Memory Usage: 15.5 MB, less than 18.61% of Python3 online submissions for Matrix Block Sum.
"""
# Using more intense prefix sum
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat[0]), len(mat)

        ans = [[0] * M for _ in range(N)]
        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for i in range(M):
            for j in range(N):
                dp[j + 1][i + 1] = (
                    dp[j + 1][i] + dp[j][i + 1] - dp[j][i] + mat[j][i]
                )

        for i in range(M):
            for j in range(N):
                i1, j1 = max(i - k, 0), max(j - k, 0)
                i2, j2 = min(i + k + 1, M), min(j + k + 1, N)

                ans[j][i] = dp[j2][i2] - dp[j2][i1] - dp[j1][i2] + dp[j1][i1]

        return ans


"""
Runtime: 1290 ms, faster than 14.75% of Python3 online submissions for Matrix Block Sum.
Memory Usage: 15.4 MB, less than 40.49% of Python3 online submissions for Matrix Block Sum.
"""
# Some improvement using prefix sum
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat[0]), len(mat)

        ans = [[0] * M for j in range(N)]

        # store prefix sums
        # leave rows of 0 on the side
        horizontal = [[0] * (M + 1) for j in range(N + 1)]
        for j in range(N):
            prefix_sum = 0
            for i in range(M):
                prefix_sum += mat[j][i]
                horizontal[j + 1][i + 1] = prefix_sum

        # fill it in
        for i in range(M):
            for j in range(N):
                prefix_sum = 0
                for l in range(
                    min(max(j - k + 1, 0), N + 1),
                    min(max(j + k + 2, 0), N + 1),
                    1,
                ):
                    prefix_sum += (
                        horizontal[l][min(max(i + k + 1, 0), M)]
                        - horizontal[l][min(max(i - k, 0), M)]
                    )

                ans[j][i] = prefix_sum

        return ans


"""
Runtime: 8243 ms, faster than 9.14% of Python3 online submissions for Matrix Block Sum.
Memory Usage: 15.2 MB, less than 85.73% of Python3 online submissions for Matrix Block Sum.
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat[0]), len(mat)

        ans = [[0] * M for j in range(N)]

        for i in range(M):
            for j in range(N):
                ans[j][i] = sum(
                    [
                        mat[jj][ii]
                        for ii in range(max(i - k, 0), min(i + k + 1, M))
                        for jj in range(max(j - k, 0), min(j + k + 1, N))
                    ]
                )

        return ans
