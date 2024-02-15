# deque is recommended for implementing stack operations in python

# deque can be used similarly as a list
# it also has methods for queue
# make sure ignoring methods that has 'left' in it 

from collections import deque

stack = deque()
stack.append('www.abc.com')
stack.append('www.abc.com/1')
stack.append('www.abc.com/2')
stack.append('www.abc.com/3')

print(stack)

print(stack.pop())
