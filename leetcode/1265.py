"""
Runtime: 36 ms, faster than 68.20% of Python3 online submissions for Print Immutable Linked List in Reverse.
Memory Usage: 15.1 MB, less than 28.44% of Python3 online submissions for Print Immutable Linked List in Reverse.
"""
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if not head:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()
