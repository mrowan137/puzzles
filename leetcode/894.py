"""
Runtime: 240 ms, faster than 34.10% of Python3 online submissions for All Possible Full Binary Trees.
Memory Usage: 23.1 MB, less than 27.46% of Python3 online submissions for All Possible Full Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if not n % 2:
            return []
        if n == 1:
            return [TreeNode()]

        m, n_orig = 0, n  # m + n = n_orig
        res = []
        while n >= 2:
            n -= 2
            m = n_orig - n - 1
            dp_m = self.allPossibleFBT(m)
            dp_n = self.allPossibleFBT(n)
            res += [
                TreeNode(left=t_m, right=t_n) for t_m in dp_m for t_n in dp_n
            ]
            # for t_m in dp_m:
            #    for t_n in dp_n:
            #        r = TreeNode()
            #        r.left, r.right = t_m, t_n
            #        res.append(r)

        return res
