"""
Runtime: 204 ms, faster than 53.67% of Python3 online submissions for LRU Cache.
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt, self.prv = None, None

    def info(self):
        print(self.key, self.value)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.size = 0
        self.head, self.tail = ListNode(-1, -1), ListNode(-1, -1)
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            self._add(key, self.dic[key].value)
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self._add(key, value)

        # remove tail if past capacity
        if self.size > self.capacity:
            self._remove()

    def _add(self, key, value):
        if key in self.dic:
            # 1. key exists
            tmp = self.dic[key]
            tmp.value = value

            # fix the connection
            prv, nxt = tmp.prv, tmp.nxt
            prv.nxt, nxt.prv = nxt, prv
        else:
            # 2. new key
            tmp = ListNode(key, value)
            self.size += 1

        # move to beginning
        new_next = self.head.nxt
        tmp.nxt = new_next
        new_next.prv = tmp
        self.head.nxt = tmp
        tmp.prv = self.head

        self.dic[key] = tmp

    def _remove(self):
        tmp, nxt = self.tail.prv, self.tail
        tmp.prv.nxt = tmp.nxt
        tmp.nxt.prv = tmp.prv
        del self.dic[tmp.key]
        self.size -= 1

    def get_list(self):
        # prints the linked list as a list
        tmp = self.head
        res = []
        while tmp:
            res.append(tmp.value)
            tmp = tmp.nxt
        print(res)


"""     
# Test example
c = LRUCache(3)
c.get_list()
c.put(1,11)
c.get_list()
c.put(2,12)
c.get_list()
c.put(3,13)
c.get_list()
c.put(1,11)
c.get_list()

c.get(3)
c.get_list()

c.put(4, 14)
c.get_list()

c.get(1)
c.get_list()
"""
