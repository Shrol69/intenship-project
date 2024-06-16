class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_front(self, node):
        self.remove_node(node)
        self.add_to_front(node)

    def remove_tail(self):
        if self.tail.prev != self.head:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node
        return None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dll = DoublyLinkedList()
        self.size = 0

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.dll.move_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dll.move_to_front(node)
        else:
            if self.size == self.capacity:
                tail_node = self.dll.remove_tail()
                if tail_node:
                    del self.cache[tail_node.key]
                    self.size -= 1
            new_node = Node(key, value)
            self.dll.add_to_front(new_node)
            self.cache[key] = new_node
            self.size += 1

    def display(self):
        node = self.dll.head.next
        print("Current LRU Cache State:")
        while node != self.dll.tail:
            print(f"({node.key}: {node.value})", end=" -> ")
            node = node.next
        print("NULL")

# Example usage
if __name__ == "__main__":
    lru_cache = LRUCache(3)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.display()  # Should display the cache in the order 3 -> 2 -> 1

    print(lru_cache.get(2))  # Accessing key 2 should move it to the front
    lru_cache.display()  # Should display the cache in the order 2 -> 3 -> 1

    lru_cache.put(4, 4)  # This should evict the least recently used key 1
    lru_cache.display()  # Should display the cache in the order 4 -> 2 -> 3

    print(lru_cache.get(1))  # Accessing key 1 should return -1 since it was evicted

    lru_cache.put(5, 5)  # This should evict the least recently used key 3
    lru_cache.display()  # Should display the cache in the order 5 -> 4 -> 2
