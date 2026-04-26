class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is Empty")
        
        val = self.top.val
        self.top = self.top.next
        self.size = -1

        return val
    

s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.pop())  # 'c'
print(s.pop())  # 'b'