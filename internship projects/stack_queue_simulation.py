class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"Popped {removed_item} from stack")
            return removed_item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack elements are:", self.stack)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued {removed_item} from queue")
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Front element is {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    def display(self):
        if not self.is_empty():
            print("Queue elements are:", self.queue)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0


# Example usage
if __name__ == "__main__":
    # Stack Operations
    print("\n--- Stack Operations ---")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()

    # Queue Operations
    print("\n--- Queue Operations ---")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    queue.peek()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
