class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def IsEmpty(self):
        if self.head == None:
            print("List is empty")
            return
        

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.IsEmpty():
            self.insert_at_beginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)


    def getCount(self):
        self.IsEmpty()
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+= 1
        return count
    

    def check_index(self, index):
        if index < 0 or index >= self.getCount():
            print("Invalid index")
            return
    

    def insert_at(self, index, data):
        self.IsEmpty()
        self.check_index(index)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            itr = itr.next
            count += 1


    def remove_at(self, index):
        self.IsEmpty()
        self.check_index(index)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1


    def displayList(self):
        self.IsEmpty()
        itr = self.head
        listString = ''
        while itr:
            listString = listString + str(itr.data) + '-->'
            itr = itr.next
        return listString

if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beginning(5)
    l.insert_at_beginning(3)
    l.insert_at_end(6)
    l.insert_at(2,100)
    l.remove_at(4)
    mylist = l.displayList()
    print(mylist)
    print(f'Length of the list is {l.getCount()}')