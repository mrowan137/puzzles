"""
Runtime: 732 ms, faster than 30.35% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.8 MB, less than 49.32% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.nums:
            return False
        self.nums[self.idx[val]] = self.nums[-1]
        self.idx[self.nums[self.idx[val]]] = self.idx[val]
        self.nums.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


"""
Runtime: 464 ms, faster than 74.51% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.4 MB, less than 95.62% of Python3 online submissions for Insert Delete GetRandom O(1).
"""
# O(1) operations using dict and list
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.num_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False
        self.num_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.num_to_idx:
            return False

        # overwrite val with val at last idx
        self.nums[self.num_to_idx[val]] = self.nums[-1]
        self.num_to_idx[self.nums[-1]] = self.num_to_idx[val]
        self.nums.pop()
        del self.num_to_idx[val]
        return True

    def getRandom(self) -> int:
        i = random.choice(range(len(self.nums)))
        return self.nums[i]


# TLE using linked list
import random


class Node:
    def __init__(self, val=None, nxt_node=None):
        self.val, self.nxt_node = val, nxt_node

    def nxt(self):
        return self.nxt_node


class RandomizedSet:
    def __init__(self):
        self.head = Node()
        self.sz = 0

    def insert(self, val: int) -> bool:
        curr = self.head
        while curr.nxt():
            if val == curr.nxt().val:
                return False
            curr = curr.nxt()
        curr.nxt_node = Node(val=val)
        self.sz += 1
        return True

    def remove(self, val: int) -> bool:
        curr, nxt = self.head, self.head.nxt()
        while curr and nxt:
            if nxt.val == val:
                curr.nxt_node = nxt.nxt()
                self.sz -= 1
                return True
            curr, nxt = curr.nxt(), nxt.nxt()

        return False

    def getRandom(self) -> int:
        N = random.choice(range(1, self.sz + 1))
        curr = self.head
        for _ in range(N):
            curr = curr.nxt()
        return curr.val


"""
Runtime: 100 ms, faster than 59.48% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 18.4 MB, less than 60.05% of Python3 online submissions for Insert Delete GetRandom O(1).
"""

import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.dic:
            return False

        # overwrite the value, update index
        self.list[self.dic[val]] = self.list[-1]  # last --> val
        self.dic[self.list[-1]] = self.dic[val]  # update idx
        self.list.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
# using linked list
# this is really O(N) so it is slow but still good practice using linked list
import random

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class RandomizedSet:
    def __init__(self):
        self.head = ListNode(-1)
        self.length = 0

    def insert(self, val: int) -> bool:
        prev, curr = self.head, self.head.next
        while curr:
            if curr.val == val: 
                return False
            
            prev, curr = curr, curr.next
            
        prev.next = ListNode(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        prev, curr = self.head, self.head.next
        while curr:
            if curr.val == val: 
                # delete node, update length
                prev.next = curr.next
                self.length -= 1
                return True
            
            prev, curr = curr, curr.next
            
        return False

    def getRandom(self) -> int:
        # choose randomly from indices
        i = randint(0, self.length - 1)
        
        # go to that index and return it 
        curr = self.head.next
        for _ in range(i): curr = curr.next
        return curr.val
"""
