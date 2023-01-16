"""
Runtime: 124 ms, faster than 27.59% of Python3 online submissions for Min Stack.
Memory Usage: 19.3 MB, less than 6.36% of Python3 online submissions for Min Stack.
"""


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.nxt = None


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy_head = LinkedList(-1)
        self.m = float("inf")

    def push(self, val: int) -> None:
        nxt = self.dummy_head.nxt
        self.dummy_head.nxt = LinkedList(val)
        self.dummy_head.nxt.nxt = nxt
        self.m = min(self.m, val)

    def pop(self) -> None:

        self.dummy_head.nxt = (
            self.dummy_head.nxt.nxt if self.dummy_head.nxt.nxt else None
        )

        # find the new min
        m = float("inf")
        curr = self.dummy_head.nxt
        while curr:
            m = min(m, curr.val)
            curr = curr.nxt

        self.m = m

    def top(self) -> int:
        return self.dummy_head.nxt.val

    def getMin(self) -> int:
        return self.m


# heap and queue
"""
Runtime: 72 ms, faster than 37.91% of Python3 online submissions for Min Stack.
Memory Usage: 18.1 MB, less than 53.55% of Python3 online submissions for Min Stack.
"""
import heapq


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        heapq.heapify(self.heap)
        self.queue = []

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        self.queue.append(val)

    def pop(self) -> None:
        self.queue.pop(-1)
        self.heap = [v for v in self.queue]
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        small = heapq.heappop(self.heap)
        heapq.heappush(self.heap, small)
        return small
