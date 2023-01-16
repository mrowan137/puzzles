"""
Runtime: 691 ms, faster than 32.94% of Python3 online submissions for Binary Trees With Factors.
Memory Usage: 14 MB, less than 94.12% of Python3 online submissions for Binary Trees With Factors.
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)

        # let dp[i] is the number of factored
        # binary trees where arr[i] as the root
        dp = [1] * N
        nodeToIndex = {a: i for i, a in enumerate(arr)}

        # if dp[j], dp[k] are the number of ways to
        # build the l and r children, dp[i] = dp[j]*p[k]
        for i in range(N):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # arr[j] divides arr[i] is left child
                    r = arr[i] / arr[j]  # arr[i]/arr[j] i the right child
                    if r in nodeToIndex:
                        dp[i] += dp[j] * dp[nodeToIndex[r]]

        return sum(dp) % (10 ** 9 + 7)
