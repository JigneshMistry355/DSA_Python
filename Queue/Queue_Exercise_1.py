from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self, data):
        self.buffer.appendleft(data)

    def pop(self):
        return self.buffer.pop()
    
    def printQueue(self):
        return print(self.buffer)
        
if __name__ == '__main__':
    q = Queue()

    Food = ['pizza', 'sandwich', 'samosa', 'Dosa']

    def Place(Food):
        for i in Food:
            q.push(i)
            print("push::",i )
            time.sleep(0.5)

    def Serve():
        time.sleep(1)
        while True:
            print("Serving your Order : ",q.pop())
            time.sleep(2)
            
    
    # PlacedOrder = placeOrder(Food)
    # PlacedOrder.printQueue()
    t = time.time()
    t1 = threading.Thread(target=Place, args=(Food,))
    t2 = threading.Thread(target=Serve,)

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()


    

