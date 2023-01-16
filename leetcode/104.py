"""
Runtime: 36 ms, faster than 90.07% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.4 MB, less than 9.69% of Python3 online submissions for Maximum Depth of Binary Tree.
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0

            return 1 + max(helper(node.left), helper(node.right))

        return helper(root)
