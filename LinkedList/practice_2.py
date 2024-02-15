class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, data, index):
        if index < 0 or index >= self.getCount()+1:
            raise Exception(f"Index range invalid\nTry to enter index between 0 and {self.getCount()} inclusively")
        if self.head == None or index == 0:
            self.insert_at_beginning(data)
            return
        if index == self.getCount():
            self.insert_at_end(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if self.head == None:
            print("list is empty")
        if index < 0 or index >= self.getCount():
            raise Exception(f"Index range invalid\nTry to enter index between 0 and {self.getCount()-1} inclusively")
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def getCount(self):
        if self.head == None:
            print("List is empty")
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def displayList(self):
        if self.head == None:
            print("\nThe list is empty")
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
    print(l.displayList())
    print(l.getCount())
    l.insert_at(6,2)
    print(l.displayList())
    print(l.getCount())
    l.insert_at(10,2)
    print(l.displayList())
    print(l.getCount())
    l.remove_at(4)
    print(l.displayList())
    print(l.getCount())
