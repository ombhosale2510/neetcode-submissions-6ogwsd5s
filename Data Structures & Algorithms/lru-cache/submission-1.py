"""
make DS which follows the LRU eviction policy
maintain usage order , doubly linked list
do in O(1) time , use hashmap lookup
evict LRU item when full capacity
"""

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail # dummy
        self.tail.prev = self.head # dummy
        # everything else enters between head and tail

    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        # remove a node from the list
        # [1,*2*,4]
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        # if exists, return node, make it recently used, else -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        # todo recently used, place at beginning
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # to update by removing first
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # remove lru
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

