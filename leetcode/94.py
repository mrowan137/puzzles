"""
Runtime: 32 ms, faster than 52.77% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.2 MB, less than 74.98% of Python3 online submissions for Binary Tree Inorder Traversal.
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # in order: me, left, right
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )
