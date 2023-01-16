"""
Runtime: 433 ms, faster than 53.75% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
Memory Usage: 83.2 MB, less than 5.07% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
"""


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # compute the full product
        # store sum of all below me
        def fullSum(root, memo):
            if not root:
                return 0
            res = (
                root.val + fullSum(root.left, memo) + fullSum(root.right, memo)
            )
            memo[root] = res
            return res

        memo = {}
        total = fullSum(root, memo)

        def findBiggestProduct(root, biggestProduct=float("-inf")):
            if not root:
                return biggestProduct
            s = memo[root]
            s_c = total - s
            biggestProduct = max(biggestProduct, s * s_c)
            biggestProductLeft = findBiggestProduct(root.left, biggestProduct)
            biggestProductRight = findBiggestProduct(root.right, biggestProduct)
            return max(biggestProduct, biggestProductLeft, biggestProductRight)

        return int(findBiggestProduct(root) % (1e9 + 7))
