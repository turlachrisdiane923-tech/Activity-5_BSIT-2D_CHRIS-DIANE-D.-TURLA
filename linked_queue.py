class Node:
    """A basic node class for a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    """Queue implemented using a singly linked list with head and tail references."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"Queue (front to rear): [{' -> '.join(elements)}]"

