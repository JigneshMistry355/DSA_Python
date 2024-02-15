class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def printListEmpty(self):
        return 'The list is empty'
    
    def getCount(self):
        if self.isEmpty():
            return 0
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count 
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1

    def insert_at_end(self, data):
        if self.isEmpty():
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def remove_at(self, index):
        if self.isEmpty():
            return self.printListEmpty()
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1 

    def displayList(self):
        if self.isEmpty():
            return self.printListEmpty()
        itr = self.head
        listString = ''
        while itr:
            listString = listString + str(itr.data) + '-->'
            itr = itr.next
        return listString


if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beginning(1)
    l.insert_at_end(2)
    l.insert_at_end(3)
    l.insert_at(0, 5)
    l.remove_at(2)
    print(l.displayList())
    print(l.getCount())
    