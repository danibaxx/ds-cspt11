"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# first in, last out or last in, first out
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output = ''
        curr_node = self.head
        while curr_node is not None:
            output += f'{curr_node.value} -> '
            curr_node = curr_node.next
        return output

    # add to head
    def add_to_head(self, value):
        new_node = Node(value)
        # checking if head/tail is none
        if self.head is None and self.tail is None:
            # setting new node to head/tail (pointer)
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # remove head
    def remove_head(self):
        # if head is empty return None
        if not self.head:
            return None
        # check if head.next is none
        if self.head.next is None:
            # hold self.head.value to variable
            head_value = self.head.value
            # set head/tail to None -> removing
            self.head = None
            self.tail = None
            # return head value
            return head_value
        # holding self.head.value in head_value
        head_value = self.head.value
        # setting self.head to self.head.next
        self.head = self.head.next
        # return head value
        return head_value


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_head()
        return node

# stack list
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         num = self.storage.pop(0)
#         return num

new_stack = Stack()
print(len(new_stack))

new_stack.push(2)
new_stack.push(4)
new_stack.push(6)
print(len(new_stack))
print(new_stack.storage)

new_stack.pop()
print(new_stack.storage)
