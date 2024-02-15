class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printIsEmpty(self):
        print('The List is Empty')
        return

    def isEmpty(self):
        return self.head == None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.isEmpty():
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_Length(self):
        if self.isEmpty():
            return 0
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def check_index(self, index):
        if index < 0 or index > self.get_Length():
            print('Invalid Index')
            return

    def insert_at(self, index, data):
        self.check_index(index)
    
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if self.isEmpty():
            return self.printIsEmpty()
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def displayList(self):
        if self.isEmpty():
            return self.printIsEmpty()
        itr = self.head
        listString = ''
        while itr:
            listString = listString + str(itr.data) + '-->'
            itr = itr.next
        return listString


if __name__ == '__main__':
    l = LinkedList()

    l.insert_at_beginning(5)
    l.insert_at_beginning(6)
    l.insert_at_beginning(7)

    l.insert_at(0, 9)
    l.insert_at(4,12)

    l.insert_at_end(11)
    l.insert_at(5,10)

    l.remove_at(5)

    length = l.get_Length()
    print(length)
    result = l.displayList()
    print(result)