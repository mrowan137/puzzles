"""
Runtime: 28 ms, faster than 83.99% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.3 MB, less than 48.72% of Python3 online submissions for Unique Binary Search Trees.
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] is number of unique trees of size i
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            l, r = 0, i - 1
            while r >= 0:
                dp[i] += dp[l] * dp[r]
                l += 1
                r -= 1

        return dp[-1]


"""
Runtime: 32 ms, faster than 61.59% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.2 MB, less than 46.64% of Python3 online submissions for Unique Binary Search Trees.
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] is the number of unique BST with i nodes
        dp = [0] * (n + 1)

        # initialize
        dp[0] = 1  # one unique way to have a tree of 0 nodes

        # adding one node, we can distribute the nodes of size n-1 as left and right subtree
        for i in range(1, n + 1):
            # 3 = 1 + 2 + 0
            #   = 1 + 1 + 1
            #   = 1 + 0 + 2
            # dp[3] = dp[2]*dp[0] + dp[1]*dp[1] + dp[0]*dp[2]
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


"""
TLE
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # base case
        if n <= 1:
            return 1

        # 1 node for me, then n-1 nodes to distribute
        # across the left and right subtrees
        res = 0
        for i in range(n):
            n_left = i
            n_right = n - 1 - i
            res += self.numTrees(n_left) * self.numTrees(n_right)

        return res
