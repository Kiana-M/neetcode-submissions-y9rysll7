class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        #insert after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
       

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add_to_front(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self._add_to_front(self.cache[key])
        else:
            if len(self.cache)>=self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            self.cache[key] = Node(key, value)
            self._add_to_front(self.cache[key])
            


        
