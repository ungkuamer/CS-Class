# for linked list, we must maintain a manual count 
# garbage collection is automatic in python (will automatically handle the abandoned node)

# create new instance of node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data # read current node data
        self.next = next # pointer for next element

# create new instance of linked list
class LinkedList:

    def __init__(self):
        self.head = None # first node (head) has none value

    # insert data at front
    def insert_at_front(self, data):
        node = Node(data, self.head) # next value of node will be current header
        self.head = node
    
    # insert data at back
    def insert_at_back(self, data):
        if self.head == None: # if list is blank, added data will be the head
            self.head = Node(data, None)
            return

        curr_head = self.head
        while curr_head.next:
            curr_head = curr_head.next # change last element pointer to new node
        
        curr_head.next = Node(data, None)
    
    # insert list of data (will wipe current list)
    def insert_multiple(self, data_list):
        self.head = None # clearing current list
        for data in data_list:
            self.insert_at_back(data)

    # insert data at specified index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_front(data)
            return
        
        count = 0
        curr_head = self.head
        while curr_head:
            if count == index - 1: # modify the pointer of previous node to point at new node
                node = Node(data, curr_head.next)
                curr_head.next = node
                break

            curr_head = curr_head.next
            count += 1

    # deleta data at specified index
    def delete_at(self, index):
        if index < 0 and index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr_head = self.head
        while curr_head:
            if count == index - 1: # stop at previous node to update the pointer to the new node
                curr_head.next = curr_head.next.next
                break

            curr_head = curr_head.next
            count += 1
    
    # delete entire linked list
    def delete_all(self):
        self.head = None

    # show the current linked list
    def print(self):
        if self.head == None:
            print('Linked List is empty')
            return

        curr_head = self.head
        link_list_str = ''
        while curr_head: # iterate through the linked list
            link_list_str += str(curr_head.data) + ' --> ' 
            curr_head = curr_head.next

        print(link_list_str)

    # get the int length of the linked list
    def get_length(self):
        count = 0
        curr_head = self.head
        while curr_head:
            count += 1
            curr_head = curr_head.next

        return count
        
# start operation here
new_list = LinkedList()
new_list.print()