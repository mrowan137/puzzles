"""
Runtime: 350 ms, faster than 32.85% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 18 MB, less than 11.74% of Python3 online submissions for Deepest Leaves Sum.
"""


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        wheelbarrow = []

        def dig(root, d=0):
            if not root:
                return 0
            if not root.left and not root.right:
                wheelbarrow.append([root.val, d])
                return
            dig(root.left, d + 1)
            dig(root.right, d + 1)

        dig(root)
        m = max(wheelbarrow, key=lambda wb: wb[1])[1]

        res = 0
        for wb in wheelbarrow:
            res += wb[0] if wb[1] == m else 0

        return res
