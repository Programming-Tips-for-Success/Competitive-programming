
# problems
# Counting Nodes in a Circular List
# Printing the contents of a circular list
# Inserting a Node at the End of a Circular Linked List
# Inserting a Node at Front of a Circular Linked List
# Deleting the Last Node in a Circular List
# Deleting the First Node in a Circular List
#  use circular lists for implementing stacks and queues - great application

class linkedListNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        return
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = linkedListNode(None)    
    self.tail = linkedListNode(None)    
    self.head.nextval = self.tail    
    self.tail.nextval = self.head    
        
  #This function will add the new node at the end of the list.    
  def add(self,data):    
    newNode = linkedListNode(data)    
    #Checks if the list is empty.    
    if self.head.dataval is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode    
      self.tail = newNode    
      newNode.nextval = self.head    
    else:    
      #tail will point to new node.    
      self.tail.nextval = newNode    
      #New node will become new tail.    
      self.tail = newNode    
      #Since, it is circular linked list tail will point to head.    
      self.tail.nextval = self.head    
     
  #Displays all the nodes in the list    
  def display(self):    
    current = self.head    
    if self.head is None:    
      print("List is empty")    
      return    
    else:    
        print("Nodes of the circular linked list: ")    
        #Prints each node by incrementing pointer.    
        print(current.dataval),    
        while(current.nextval != self.head):    
            current = current.nextval    
            print(current.dataval),    
     
     
class CircularLinkedList:    
  cl = CreateList()    
  #Adds data to the list    
  cl.add(1)    
  cl.add(2)    
  cl.add(3)    
  cl.add(4)    
  #Displays all the nodes present in the list    
  cl.display() 


