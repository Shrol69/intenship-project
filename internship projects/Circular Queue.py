class CircularQueue:
    def __init__(self, size):
        self.size = size  
        self.queue = [None] * size 
        self.front = self.rear = -1  

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.front == -1: 
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value 
            print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            value = self.queue[self.front] 
            if self.front == self.rear: 
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            print(f"Dequeued: {value}")
            return value

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements are:", end=" ")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i], end=" ")
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.queue[i], end=" ")
            print()  

# Example usage:
if __name__ == "__main__":
    cq = CircularQueue(5)

    # Enqueue elements
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)  # This should fill the queue

    # Display elements
    cq.display()

    # Dequeue an element
    cq.dequeue()
    cq.display()

    # Enqueue another element (should work due to circular nature)
    cq.enqueue(60)
    cq.display()

    # Dequeue more elements
    cq.dequeue()
    cq.dequeue()
    cq.display()
