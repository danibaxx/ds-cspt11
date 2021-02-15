"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
# DRAW ALL OF THE METHODS OUT FIRST BEFORE CODING, then UPER them
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        output = 'DLL: [ '
        curr_node = self.head
        while curr_node is not None:
            output += ' <=> ' if curr_node.prev else ''
            output += f'{curr_node}'
            curr_node = curr_node.next
        return output + ']'
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        # increment list by 1
        self.length += 1
        # check if head/tail is None
        if self.head is None and self.tail is None:
            # set head/tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # set self.head is new node next
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return None
        self.length += 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    # check if there is nodes in the DLL
    # if length == 0 return None
    # if length == 1 return self.head.value
    # current_max starts out as self.head.value or None
    # iterate through the DLL to find max value
    # need current_max variable
    # compare current_max to each value and update current_max if value > current_max
    # return current_max
    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        current_max = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_max < current_node.value:
                current_max = current_node.value
            current_node = current_node.next
        return current_max

d_l_l = DoublyLinkedList()
print(d_l_l)

d_l_l.add_to_head(2)