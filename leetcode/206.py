"""
Runtime: 32 ms, faster than 86.43% of Python3 online submissions for Reverse Linked List.
Memory Usage: 16.3 MB, less than 26.39% of Python3 online submissions for Reverse Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head_r = ListNode(-1)
        while head:
            tmp = head_r.next
            head_r.next = ListNode(head.val)
            head_r.next.next = tmp
            head = head.next

        return head_r.next
