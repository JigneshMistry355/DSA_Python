# Consider this class as a diagram of a single node with data and address in two parts of a box
class Node:
    def __init__(self, data = None, next = None):
        self.data = data # This is the left box of any node
        self.next = next # This is the right box of any node that points to the next element in the list

# This class is the blueprint of the collection of multiple nodes
class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        # if we want to insert a node at the beginning of the list
        # the node will take the data and point to the head of the list
        # So while creating node object we pass parameters as --data and --self.head and Not --self.next
        node = Node(data, self.head)
        # Once the node is placed at the beginning of the list, it has to be announced as head
        self.head = node


    def insert_at_Last(self, data):
        # When there exists no node in the list
        # the node created becomes the only node in the list
        if self.head is None:
            # So the node comes with the data and next address as NONE
            # Because last node in llinked list has no next address
            self.head = Node(data, None)
            return
        # Initially point an iterator to head
        itr = self.head
        # iterate through the whole list
        while itr.next:
            # traverse list untill itr.next in Not null
            itr = itr.next
        # Once itr.next is null, point the next of last element to the new node
        itr.next = Node(data, None)


    # This function enters elements into an empty linked List
    def insert_list(self, my_list):
        self.head = None
        for data in my_list:
            self.insert_at_Last(data)


    # Function to get the length of the list
    def get_length(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter
    

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        # if the element to be removed is at index 0, then make element at index 1 as head
        # garbage collection is taken by python itself
        # in other languages garbage collection may or may not be done automatically
        if index == 0:
            self.head = self.head.next

        counter = 0
        # let the iterator start from head, it is at head 
        itr = self.head
        # the iteration starts
        while itr:
            # suppose index 2 is to be reomved
            # when at index 1, ie counter == 1
            # the element at index one will point to index 3 using --> itr.next.next
            # it will ignore index 2 and hence element at index 2 is removed
            if counter == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next



    def displayList(self):
        if self.head is None:
            print("The list is empty")
            return
        # I take an iterator and assign it an initial position
        itr = self.head
        # creating an empty variable to store data to be printed
        list_str = ''
        # Now i want this iterator to go through the whole list
        while itr:
            list_str = list_str + str(itr.data) + '-->'
            itr = itr.next
        print(list_str)



if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_beginning(5)
    l.insert_at_beginning(7)
    l.insert_at_beginning(3)
    l.insert_at_Last(100)

    my_list = ['A','B','C','D']
    # This function removes previous elements and adds new elements 
    l.insert_list(my_list)

    l.insert_at_beginning(88)
    l.displayList()
    print("Length: ", l.get_length())
    l.remove_at(0)
    l.displayList()


