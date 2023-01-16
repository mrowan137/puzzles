"""
Runtime: 64 ms, faster than 89.02% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        curr = head
        carry = 0
        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next

            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next

            tmp += carry
            carry, add = divmod(tmp, 10)

            curr.val += add

        if carry:
            curr.next = ListNode()
            curr = curr.next
            curr.val += carry

        return head.next
