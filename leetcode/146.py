"""
Runtime: 1486 ms, faster than 20.81% of Python3 online submissions for LRU Cache.
Memory Usage: 76.2 MB, less than 51.32% of Python3 online submissions for LRU Cache.
"""


class Node:
    def __init__(self, k, v, nxt=None, prv=None):
        self.k, self.v = k, v
        self.nxt, self.prv = nxt, prv


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_node = {}
        self.head = Node("@", "#")
        self.tail = Node("@", "#")
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self._remove(key)
            self._add(key)
            return self.key_to_node[key].v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._remove(key)
            self._add(key)
            self.key_to_node[key].v = value
        else:
            n = Node(key, value)
            self.key_to_node[key] = n
            self._add(key)
            if len(self.key_to_node) > self.cap:
                k = self.tail.prv.k
                self._remove(self.tail.prv.k)
                del self.key_to_node[k]

    def _add(self, key):
        # add at the first spot
        # assumes the node is already in map
        curr = self.key_to_node[key]
        nxt = self.head.nxt
        curr.nxt = nxt
        curr.prv = self.head
        self.head.nxt = curr
        nxt.prv = curr

    def _remove(self, key):
        # remove node at the given spot
        # assum node is already in map
        curr = self.key_to_node[key]
        nxt, prv = curr.nxt, curr.prv
        prv.nxt = nxt
        nxt.prv = prv
        curr.nxt = None
        curr.prv = None


"""
Runtime: 952 ms, faster than 35.99% of Python3 online submissions for LRU Cache.
Memory Usage: 77.1 MB, less than 5.57% of Python3 online submissions for LRU Cache.
"""


class Node:
    def __init__(self, k, v):
        self.val = v
        self.key = k
        self.prv = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        # Use a doubly linked list to track order, i.e.
        # history of accesses; use dict for fast k-v access
        self.cap = capacity
        self.dic = dict()  # input a key, get the node
        self.tail = Node(-1, -1)
        self.head = Node(-1, -1)
        self.tail.prv = self.head
        self.head.nxt = self.tail

    def get(self, key: int) -> int:
        # the key is not present:
        if not key in self.dic.keys():
            return -1

        # the key is present:
        n = self.dic[key]
        self._remove(n)  # pop it from the list
        self._add(n)  # add it back at the head
        # k-v is the same so don't touch dict
        return n.val

    def put(self, key: int, value: int) -> None:
        # ll if it's present
        # don't need to del from dic, overwrite val later
        if key in self.dic.keys():
            self._remove(self.dic[key])

        # add a new node
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n

        # if past capacity, evict LRU
        if len(self.dic.keys()) > self.cap:
            del self.dic[self.tail.prv.key]
            self._remove(self.tail.prv)

    def _remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt = nxt
        nxt.prv = prv

    def _add(self, node):
        nxt = self.head.nxt
        self.head.nxt = node
        node.nxt = nxt
        node.prv = self.head
        nxt.prv = node
