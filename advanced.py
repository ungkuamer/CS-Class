# initialise node class
class node:
    def __init__(self, data=None): # passing data point to be stored by node
        self.data = data
        self.next = None # store pointer to the next node -- initialise to 'none' 

class linked_list:
    def __init__(self):
        self.head = node() # always have a head node and this is not a data node

    def append(self, data): # use to create first element of the list
        new_node = node(data)
        curr = self.head

        while curr.next != None: 
            curr = curr.next # go to next node

        curr.next = new_node

    def length(self): # use to check length
        curr = self.head
        total_num = 0

        while curr.next != None:
            total_num += 1
            curr = curr.next
    
        return total_num

    def display(self):
        elements = []
        curr_node = self.head
        
        while curr_node.next != None:
            curr_node = curr_node.next
            elements.append(curr_node.data)

        print(elements)

my_list = linked_list()


my_list.append(1)
my_list.append(2)

my_list.display()