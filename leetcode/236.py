"""
Runtime: 76 ms, faster than 41.54% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 25.2 MB, less than 73.60% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # strategy: pass up a target root if found; the first case this happens
        # must be the lowest common ancestor

        # if root is the LCA
        if root == p or root == q:
            return root

        # search in the left and right subtrees
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # root must be the LCA
            return root
        else:
            # send up whichever branch found a target
            return left or right


"""
Runtime: 1672 ms, faster than 5.09% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 28.4 MB, less than 9.25% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # strategy: find path to p and path to q
        def helper(n, target):
            if not n:
                return []
            if n.val == target:
                return [target]

            l, r = helper(n.left, target), helper(n.right, target)
            add = l if target in l else r
            return [n.val] + add

        p_anc = helper(root, p.val)
        q_anc = helper(root, q.val)

        i = 0
        while i < min([len(p_anc), len(q_anc)]) and p_anc[i] == q_anc[i]:
            i += 1

        return TreeNode(p_anc[i - 1])
