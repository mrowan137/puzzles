"""
Runtime: 264 ms, faster than 73.05% of Python3 online submissions for Range Sum of BST.
Memory Usage: 23.1 MB, less than 17.95% of Python3 online submissions for Range Sum of BST.
"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        add = root.val if root.val >= low and root.val <= high else 0
        return (
            add
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
