from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self, data):
        self.buffer.appendleft(data)

    def pop(self):
        return self.buffer.pop()
    
    def display(self):
        return self.buffer
    
    def size(self):
        return len(self.buffer)
    
    def isEmpty(self):
        return len(self.buffer) == 0
    

    
if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    print(q.size())
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.size())
    print(q.pop())
    print(q.display())