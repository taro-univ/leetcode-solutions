class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val):
        node = Node(val)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if self.head is None:
            self.head = node
        
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is Empty")
        
        val = self.head.val
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        self.size -= 1

        return val
    
