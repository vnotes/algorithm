class LRUCache:
    def __init__(self, capacity: int):
        __head = DoubleLinkNode(-1, -1)
        __tail = DoubleLinkNode(-1, -1)
        __head._next = __tail
        __tail.prev = __head
        self.cap = capacity
        self.table = {}
        self.head = __head
        self.tail = __tail

    def __len__(self):
        return len(self.table)

    def add_node(self, node):
        node._next = self.head._next
        self.head._next.prev = node
        node.prev = self.head
        self.head._next = node

    @staticmethod
    def remove_node(node):
        node.prev._next = node._next
        node._next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self.remove_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            node = DoubleLinkNode(key, value)
            self.add_node(node)
            self.table[key] = node
            if len(self) > self.cap:
                tail = self.pop_tail()
                del self.table[tail.key]
        else:
            node = self.table[key]
            node.value = value
            self.remove_to_head(node)

    def remove_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node


class DoubleLinkNode:
    def __init__(self, key, value):
        self.prev = None
        self._next = None
        self.key = key
        self.value = value


if __name__ == '__main__':
    lru = LRUCache(1)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(3))
