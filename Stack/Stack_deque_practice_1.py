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
    
    def display(self):
        # return [i for i in self.container] .... try 
        return self.container
    

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(7)
    s.push(2)
    print(s.display())
    print(s.pop())
    print(s.peek())
    print(s.display())

