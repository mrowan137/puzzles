"""
Runtime: 53 ms, faster than 18.73% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.1 MB, less than 76.36% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head

        def f(node):
            if not node:
                return 0
            my_place = f(node.next) + 1
            if my_place == n + 1:
                node.next = node.next.next
            return my_place

        f(dummy)

        return dummy.next


"""
Runtime: 36 ms, faster than 58.05% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 46.46% of Python3 online submissions for Remove Nth Node From End of List.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # recursive count how for I am from the end
        dummy = ListNode(-1)
        dummy.next = head

        def r(node):
            if not node:
                return 0
            cnt = r(node.next) + 1
            if cnt == n + 1:
                if node.next:
                    node.next = node.next.next
                else:
                    node.next = None
            return cnt

        r(dummy)
        return dummy.next
