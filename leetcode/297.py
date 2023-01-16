# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # strategy: encode preorder traversal
        def helper(n):
            if not n:
                return "$"
            l, r = n.left, n.right
            return str(n.val) + " " + helper(l) + " " + helper(r)

        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "$":
            return []

        data = list(data.split(" "))
        head = TreeNode(data.pop(0))

        def helper(p, dat):
            if dat:
                # construct left subtree
                v = dat.pop(0)
                if v != "$":
                    # not a null
                    p.left = TreeNode(v)
                    helper(p.left, dat)

            if dat:
                # construct right subtree
                v = dat.pop(0)
                if v != "$":
                    # not a null
                    p.right = TreeNode(v)
                    helper(p.right, dat)

            return p

        return helper(head, data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
