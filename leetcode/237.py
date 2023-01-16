"""
Runtime: 36 ms, faster than 82.25% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 15.2 MB, less than 30.58% of Python3 online submissions for Delete Node in a Linked List.
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next.next:
            node.val = node.next.val
            node.next = None
            return
        node.val = node.next.val
        self.deleteNode(node.next)
