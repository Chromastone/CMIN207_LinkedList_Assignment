from node import Node
from BoudreauxClients import Clients

class Linkedlist():
    def __init__(self):
        self.head = None

    #Methods

    def __str__(self):
        print_str = ""
        if self.head == None:
            print_str += "List is Empty!"
        else:
            traverser = self.head
            while traverser != None:
                print_str += str(traverser.data) + "\n"
                traverser = traverser.next
            
        return print_str

    def __contains__(self, target):
        traverser = self.head
        while traverser != None:
            if traverser.data.name == target:
                return True
            traverser = traverser.next
        return False    
    
    def access(self, target):
        traverser = self.head
        client_id = 0
        while traverser != None:
            if traverser.data.name == target:
                return traverser.data, client_id
            traverser = traverser.next
            client_id += 1
        return "False"

    # append()
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            currentEnd = self.head
            while currentEnd.next != None:
                currentEnd = currentEnd.next
            currentEnd.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None and position > 1:
                temp = temp.next
                position -= 1
            #temp seamingly acts as head and then we prepend to this "head"
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, position):
        if position ==0:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next != None and position > 1:
                temp = temp.next
                position -= 1
            #print(temp.next.data)
            temp.next = temp.next.next