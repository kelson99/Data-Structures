
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
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
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # probably need to add conditional logic for 
        # when their is no head etc.
        new_node = ListNode(value, None, None)
        if self.tail == None and self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif self.head.next == None:
            old_head = self.head
            old_head.prev = new_node
            new_node.next = old_head
            self.head = new_node
            self.tail = old_head
            self.length += 1
        
        else: 
            old_head = self.head
            old_head.prev = new_node
            new_node.next = old_head
            self.head = new_node
            self.length += 1


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.tail == None and self.head == None:
            return

        elif self.head.next == None:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return old_head.value

        else:
            old_head = self.head
            self.head = old_head.prev
            # old_head = None
            self.length -= 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if self.tail ==  None and self.head == None:
            # create the new head.
            self.head = new_node
            self.tail = new_node
            self.length += 1

        elif self.head.next == None:
            #add to the (head tail combonation) and set the new tail
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node
            self.length += 1

        else:
            old_tail = self.tail
            self.tail = new_node
            self.tail.prev = old_tail
            old_tail.next = new_node
            self.length += 1

        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # checks to see if it is the first element in the list
        if self.tail == None and self.head == None:
            return

        elif self.head.next == None:
            # case where there is only one element in the linked list
            old_head_tail = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return old_head_tail.value

        else:
            old_tail = self.tail
            self.tail = old_tail.prev
            self.length -= 1
            return old_tail.value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.tail == None and self.head == None:
            return
        
        elif self.head.next == None:
            return

        else:
            if self.tail == node:
                old_tail = self.tail
                self.tail = old_tail.prev
                old_head = self.head
                old_head.prev = old_tail
                self.head = old_tail
                old_tail.next = old_head
                old_tail.prev = None
            else: 
                node.next = None
                node.prev = None
                old_head = self.head
                old_head.prev = node
                self.head = node
                node.next = old_head

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail == None and self.head == None:
            return
        
        elif self.head.next == None:
            return

        else:
            if self.head == node:
                old_head = self.head
                self.head = old_head.next
                old_tail = self.tail
                old_tail.next = old_head
                self.tail = old_head
                old_head.next = None
                old_head.prev = old_tail

            else:
                node.next = None
                node.prev = None
                old_tail = self.tail
                old_tail.next = node
                self.tail = node
                node.prev = old_tail
                

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.tail == None and self.head == None:
            self.length = 0
            return None

        elif self.head.next == None:
            self.head = None
            self.tail = None
            self.length = 0
            return None

        elif self.head == node or self.tail == node:
            if self.head == node:
                old_head = self.head
                self.head = old_head.next
                self.length -= 1
                # old_head.next = None
                return old_head
            
            elif self.tail == node:
                old_tail = self.tail
                self.tail = old_tail.prev
                self.length -= 1
                return old_tail

        else:
            previous_node = node.prev
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
            self.length -= 1
            return node
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        value = self.head.value
        current = self.head

        while current is not None:
            if current.value > value:
                value = current.value

            current = current.next
        return value
        
