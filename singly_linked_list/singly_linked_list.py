class Node:
  def __init__(self, value, next=None):
    self.value = value
    # points to the next node in the list
    self.next = next 

class LinkedList:
  def __init__(self):
    # points to 1st node in list
    self.head = None 
    # points to the last node in list
    self.tail = None
    self.length = 0

# check tests -> test_singly_linked_list.py

# append / add --> add_to_tail
# UPER->
# check if theres a tail
# if tail (general case) ->
# a) create a new node with the value we want to add next = None
# b) set current tail.next to the new node
# c) set self.tail to the new node
# if no tail(empty) ->
# a) create new node
# b) set self.head and self.tail to the new node

  def add_to_tail(self, value):
    if not self.tail:
      # check length
      # check if tail == None:
      new_tail = Node(value, None)
      self.head = new_tail
      self.tail = new_tail
    else:
      new_tail = Node(value, None)
      old_tail = self.tail
      old_tail.next = new_tail
      self.tail = new_tail
    self.length += 1

# remove -> remove_head
# check if there is a head ->
# (general case): set self.head to current_head.next
# return current_head.value
# (empty): return None
# (list with one element): set self.head to current_head.next (which is also None), set self.tail to None
# decrement length -=1

  def remove_head(self):
    if not self.head:
      return None
    if self.head == self.tail:
      current_head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return current_head.value
    else:
      current_head = self.head
      self.head = current_head.next
      self.length -= 1
      return current_head.value
      
  # UPER -> 
  # check for tail(general):
  # start at head and iterate to the next-to-last node
  # a) stop when current_node.next == self.tail
  # b) save current_tail.value
  # c) set self.tail to current_tail
  # d) set current_node.next to None
  # (1 element in list):
  # save the current_tail.value
  # set self.tail to None
  # set self.head to None
  def remove_tail(self):
    if not self.tail:
      return None
    if self.tail == self.head:
      current_tail = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return current_tail.value
    else:
        current_node = self.head
        while current_node.next != self.tail:
          current_node = current_node.next
        current_tail = self.tail
        self.tail = current_node
        current_node.next = None
        self.length -= 1
        return current_tail.value

  def add_to_head(self, value):
    if self.head is None:
      new_node = Node(value, None)
      self.head = new_node
      self.tail = new_node
      self.length += 1
    else:
      new_node = Node(value, self.head)
      self.head = new_node
      self.length += 1

  def remove_at_index(self, index):
    # check length > i, if not return none
    if index >= self.length:
      return Node
    if self.length == 1 and index == 0:
      target = self.head
      self.head = None
      self.tail = None
      self.length += 1
    prev_node = self.head
    for i in range(i - 1):
      prev_node = prev_node.next
    target = prev_node.next
    prev_node.next = target.next
    self.length -= 1
    return target.value
   