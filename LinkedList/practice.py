class Node:
    def __init__(self, data=None, next=None):
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
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None) 


    def insert_at(self, data, index):
        if self.head == None:
            raise Exception('List empty')
        
        if index < 0 or index > self.get_count():
            print("\nPlease enter a valid index\n")
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        

        count = 0
        itr = self.head
        while itr:
            
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


    def get_count(self):
        if self.head == None:
            print("List is empty")
        itr = self.head 
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter
    

    def remove_at(self, index):
        if index < 0 or index > self.get_count():
            raise Exception("Invalid index")
        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
    

    def insert_list(self, my_list):
        for data in my_list:
            self.insert_at_end(data)


    def create_new_list(self, my_list):
        self.head = None
        for data in my_list:
            self.insert_at_end(data)


    def displayList(self):
        if self.head == None:
            print("Linked list is empty")

        itr = self.head
        list_string = ''
        while itr:
            list_string = list_string + str(itr.data) + '-->'
            itr = itr.next
        print(list_string)


if __name__ == '__main__':
    # creating the list
    l = LinkedList()

    print('\nThe created list is:')
    # inserting 2 elements in the beginning
    l.insert_at_beginning(1)
    l.insert_at_beginning(2)

    #inserting 1 element at the end
    l.insert_at_end(55)

    l.insert_at(100,4)

    # inserting a list at the end
    # my_list = [1,5,3,4]
    # l.insert_list(my_list)

    # removing an element from linkedlist
    # print(f'\nRemoving 3 from list {l.displayList()}')
    # l.remove_at(6)

    # displaying list after deletion

    l.displayList()

    # print the length of the string
    # print(f'\nThe length of linked list is {l.get_count()}')

    # deleting previous list and creating a new list
    # l.create_new_list(my_list)
    # print(f'\nThe new list created is --->>>   ')
    # l.displayList()
