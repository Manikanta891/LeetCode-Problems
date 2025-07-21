# from collections import OrderedDict

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # Move key to end to mark it as recently used
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)  # Remove LRU item (first one)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value #Node address is storing here
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy nodes to avoid edge case handling
        self.head = Node(0, 0)  # Least Recently Used
        self.tail = Node(0, 0)  # Most Recently Used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node #Between head and tail are real cache items.

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)  # move to tail (most recently used)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node #Storing the address of created node in place of value

        if len(self.cache) > self.capacity:
            # Remove from head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key] #Deleting the entry in dictionary


# Data structures:
# - Doubly linked list: maintains usage order, head is least recently used (LRU), tail is most recently used (MRU)
# - HashMap (cache dict): maps keys -> node addresses, for O(1) access

# Core methods:
# - _remove(node): unlinks a node from the linked list in O(1)
# - _add(node): inserts a node right before tail (MRU position) in O(1)

# get(key):
# - If key not found, return -1
# - Else, remove node from current position, add to MRU position, return value

# put(key, value):
# - If key exists, remove old node
# - Add new node at MRU position
# - If capacity exceeded, evict LRU node (head.next)
