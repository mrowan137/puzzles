"""
Runtime: 28 ms, faster than 88.49% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 72.92% of Python3 online submissions for Middle of the Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, n = head, 0
        while curr:
            curr = curr.next
            n += 1

        curr = head
        for i in range(n // 2):
            curr = curr.next

        return curr


"""
Runtime: 28 ms, faster than 87.15% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 71.97% of Python3 online submissions for Middle of the Linked List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        curr = head
        for i in range(count // 2):
            curr = curr.next

        return curr
