"""
Runtime: 52 ms, faster than 5.02% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.5 MB, less than 6.85% of Python3 online submissions for Symmetric Tree.
"""


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def cpy(n, m):
            if not m:
                return None
            n = TreeNode(m.val)
            n.left, n.right = cpy(n.left, m.left), cpy(n.right, m.right)
            return n

        def tolist(node):
            if not node:
                return [None]
            res = [node.val] + tolist(node.left) + tolist(node.right)
            return res

        def mirror(node):
            if not node:
                return
            node.left, node.right = mirror(node.right), mirror(node.left)

            return node

        x, m = cpy(TreeNode(-1), root), mirror(root)

        return tolist(x) == tolist(m)
