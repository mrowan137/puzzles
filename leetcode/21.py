"""
Runtime: 32 ms, faster than 90.36% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.2 MB, less than 60.99% of Python3 online submissions for Merge Two Sorted Lists.
"""
# iteration
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        head.next = l1 if l1 else l2

        return dummy.next


"""
Runtime: 40 ms, faster than 43.05% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.4 MB, less than 29.56% of Python3 online submissions for Merge Two Sorted Lists.
"""
# recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)

        # exit case
        if not l1 or not l2:
            return l1 if l1 else l2

        # have two link list
        if l1.val < l2.val:
            dummy.next = l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            dummy.next = l2
            l2.next = self.mergeTwoLists(l1, l2.next)

        return dummy.next


"""
Runtime: 40 ms, faster than 42.94% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14 MB, less than 95.44% of Python3 online submissions for Merge Two Sorted Lists.
"""
# iteration using in-place
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        dummy = curr = ListNode(-1)
        curr.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
                curr = curr.next
            else:
                tmp1 = curr.next  # l1 tail
                curr.next = l2
                tmp2 = l2.next  # l2 tail
                curr = curr.next
                curr.next = tmp1
                l2 = tmp2

        curr.next = l1 or l2

        return dummy.next
