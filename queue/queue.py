"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Node:
    #implicitly setting value/next to None
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        # setting the head/tail to None
        self.head = None
        self.tail = None

    def __str__(self):
        # empty string
        output = ''
        # setting head to current node
        curr_node = self.head
        # while current node is not None, return an output to show current node = next node
        # return output
        while curr_node is not None:
            output += f'{curr_node.value} <- '
            curr_node = curr_node.next
        return output

    # add to tail
    def add_to_tail(self, value):
        # create new node
        new_node = Node(value)
        # check if head/tail is none
        if self.head is None and self.tail is None:
            # setting head/tail to new_node
            self.head = new_node
            self.tail = new_node
        else:
        # then set tail's next to the new node created
            self.tail.next = new_node
            self.tail = new_node
        
    # remove from head
    def remove_head(self):
        # if not the head return none
        if not self.head:
            return None
        # check if head.next is none
        if self.head.next is None:
            # holding self.head.value to head_value
            head_value = self.head.value
            # set head/tail to None -> removing
            self.head = None
            self.tail = None
            return head_value
        # holding self.head.value in head_value
        head_value = self.head.value
        # setting self.head to self.head.next
        self.head = self.head.next
        return head_value

class Queue:
    def __init__(self):
        self.size = 0
        # using LinkedList as storage
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # increment by 1
       self.size += 1
       # adding value to tail
       self.storage.add_to_tail(value)

    def dequeue(self):
        # check is size is 0
        if self.size == 0:
            return None
        # decrement by 1
        self.size -= 1
        # removing value from head
        node = self.storage.remove_head()
        return node

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#        self.size += 1
#        self.storage.append(value)

#     def dequeue(self):
#         # check if storage is empty and return None
#         if len(self.storage) == 0:
#             return None
#         # decrement size by 1 (being removed)
#         self.size -= 1
#         num = self.storage.pop(0)
#         return num

new_queue = Queue()
print(len(new_queue))

new_queue.enqueue(2)
new_queue.enqueue(4)
new_queue.enqueue(6)
print(new_queue.storage)

new_queue.dequeue()
print(new_queue.storage)