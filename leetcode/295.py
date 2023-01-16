"""
Runtime: 336 ms, faster than 21.12% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 29.6 MB, less than 11.72% of Python3 online submissions for Find Median from Data Stream.
"""
# BST adapted from: https://leetcode.com/problems/find-median-from-data-stream/discuss/74119/18ms-beats-100-Java-Solution-with-BST
class BSTNode:
    def __init__(self, val, p):
        self.val = val
        self.p = p
        self.l, self.r = None, None

    def add(self, num):
        if num < self.val:
            if self.l:
                self.l.add(num)
            else:
                self.l = BSTNode(num, self)
        else:
            if self.r:
                self.r.add(num)
            else:
                self.r = BSTNode(num, self)

    def nxt(self):
        if self.r:
            res = self.r
            while res.l:
                res = res.l
        else:
            res = self
            while res.p.r == res:
                res = res.p
            res = res.p

        return res

    def prv(self):
        if self.l:
            res = self.l
            while res.r:
                res = res.r
        else:
            res = self
            while res.p.l == res:
                res = res.p
            res = res.p
        return res


class MedianFinder:
    def __init__(self):
        self.root = None
        self.n = 0  # keep track of number of nodes

    def addNum(self, num):
        if not self.root:
            self.root = BSTNode(num, None)
            self.tmp = self.root
        else:
            self.root.add(num)
            if not self.n % 2:  # odd number of nodes
                if self.tmp.val <= num:
                    self.tmp = self.tmp.nxt()
            else:  # even number of nodes
                if self.tmp.val > num:
                    self.tmp = self.tmp.prv()

        self.n += 1

    def findMedian(self):
        if self.n % 2:
            return self.tmp.val
        else:
            return 0.5 * (self.tmp.val + self.tmp.nxt().val)


"""
Runtime: 2756 ms, faster than 5.04% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 25.1 MB, less than 99.76% of Python3 online submissions for Find Median from Data Stream.
"""
# O(n log(n)) time
# O(n) memory
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def addNum(self, num: int) -> None:
        if not self.list:
            self.list.append(num)
        else:
            # binary search -- place num in the right location
            l, r = 0, len(self.list) - 1
            while l <= r:
                m = (l + r) // 2
                if num < self.list[m]:
                    r = m - 1
                elif num > self.list[m]:
                    l = m + 1
                else:
                    l = m
                    break
            # insert num to position m
            self.list = self.list[:l] + [num] + self.list[l:]

    def findMedian(self) -> float:
        # the list is sorted so just retrieve the middle index
        m = len(self.list) // 2
        return (
            self.list[m]
            if len(self.list) % 2 == 1
            else 0.5 * (self.list[m] + self.list[m - 1])
        )
