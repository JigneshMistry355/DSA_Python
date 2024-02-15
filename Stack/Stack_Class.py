from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def peek(self):
        return self.container[-1]
    
    def pop(self):
        return self.container.pop()
    
    def isEmpty(self):
        return len(self.container) == 0
    
    def sizeOf(self):
        return len(self.container)

    def printStack(self):
        return self.container
    

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.push(11)
    
    for i in range(s.sizeOf()):
    
        print(f'{s.pop()} is popped')
        # print(s.printStack())
        break
        

    if s.isEmpty():
        print(f'The stack is empty {s.printStack()}')
    print(s.printStack())