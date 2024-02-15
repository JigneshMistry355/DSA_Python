# list is not recommended for implementing stack operations

myList = []

# append is the push operation for a stack using list
myList.append('www.abc.com') 
myList.append('www.abc.com/1')
myList.append('www.abc.com/2')
myList.append('www.abc.com/3')

print(myList)

# pop is used to get(print) the last element from the list
# pop will also remove the last element from the list

print(myList.pop())

print(myList)
