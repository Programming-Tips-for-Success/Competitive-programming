'''
Objective
Check out the Tutorial tab for learning materials and an instructional video!
Task
A Node class is provided for you in the editor. A Node object has an integer data field,
, and a Node instance pointer,
, pointing to another node (i.e.: the next node in a list).
A removeDuplicates function is declared in your editor, which takes a pointer to the
node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.
Note: The
pointer may be null, indicating that the list is empty. Be sure to reset your
pointer when performing deletions to avoid breaking the list.
Input Format
You do not need to read any input from stdin. The following input is handled by the locked stub code and passed to the removeDuplicates function:
The first line contains an integer,
, the number of nodes to be inserted.
The subsequent lines each contain an integer describing the
value of a node being inserted at the list's tail.
Constraints
    The data elements of the linked list argument will always be in non-decreasing order.
Output Format
Your removeDuplicates function should return the head of the updated linked list. The locked stub code in your editor will print the returned list to stdout.
Sample Input
6
1
2
2
3
3
4
Sample Output
1 2 3 4 
Explanation
, and our non-decreasing list is . The values and both occur twice in the list, so we remove the two duplicate nodes. We then return our updated (ascending) list, which is .
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        current = head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

class linkedListNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        return
class SLinkedList:
    def __init__(self):
        self.headval = None
        
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def printList2(self, node): 
  
        while (node != None) : 
            print( node.dataval, end=" ") 
            node = node.nextval                   
    def AtBegining(self,newdata):
        NewNode = linkedListNode(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
        
    def AtEnd(self, newdata):
        NewNode = linkedListNode(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode  
        
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = linkedListNode(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
        
    def RemoveNode(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None
    def has_value(self, value):
        if self.headval == value:
            return True
        else:
            return False 

    def list_length(self):
        count = 0
        current_node = self.headval
        
        while current_node is not None:
            # increase counter by one
            count = count + 1
            
            # jump to the linked node
            current_node = current_node.nextval
            
        return count

    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        
        # define current_node
        current_node = self.headval
        
        # define position
        node_id = 1
        
        # define list of results
        results = []
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            # jump to the linked node
            current_node = current_node.nextval
            node_id = node_id + 1
        
        return results
    def remove_list_item_by_id(self, item_id):
        
        current_id = 1
        current_node = self.headval
        previous_node = None
        
        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (headval)
                if previous_node is not None:
                    previous_node.nextval = current_node.nextval
                else:
                    self.headval = current_node.nextval
                    # we don't have to look any further
                    return
            
            # needed for the nextval iteration
            previous_node = current_node
            current_node = current_node.nextval
            current_id = current_id + 1
        
        return
    def printParticularItem(self, index):
             printvalue = self.headval
             i = 0
             while printvalue is not None:
                 if(i== index):
                     print(printvalue.dataval)
                     return
                 printvalue = printvalue.nextval
                 i =  i + 1
    def pushData(self, newdata):
        new_Node = linkedListNode(newdata)
        new_Node.nextval = self.headval
        self.headval = new_Node
 
    
    def removeDuplicates(self): 
        temp = self.headval 
        if temp is None: 
            return
        while temp.nextval is not None: 
            if temp.dataval == temp.nextval.dataval: 
                new = temp.nextval.nextval
                temp.nextval = None
                temp.nextval = new 
            else: 
                temp = temp.nextval
        return self.headval
    
    def getMiddle(self, headval): 
        if (headval == None): 
            return headval 
  
        slow = headval 
        fast = headval 
  
        while (fast.nextval != None and 
               fast.nextval.nextval != None): 
            slow = slow.nextval
            fast = fast.nextval.nextval
              
        return slow
    def sortedMerge(self, a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.dataval <= b.dataval: 
            result = a 
            result.nextval = self.sortedMerge(a.nextval, b) 
        else: 
            result = b 
            result.nextval = self.sortedMerge(a, b.nextval) 
        return result  
    def mergeSort(self, h): 
          
        # Base case if headval is None 
        if h == None or h.nextval == None: 
            return h 
  
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.nextval
  
        # set the nextval of middle node to None 
        middle.nextval = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist
    # last item move to first place    
    def moveItems(self):
        tmp = self.headval
        sec_last = None
        while tmp and tmp.nextval : 
            sec_last = tmp 
            tmp = tmp.nextval
  
        # point the nextval of the second 
        # last node to None 
        sec_last.nextval = None
  
        # Make the last node as the first Node 
        tmp.nextval = self.headval 
        self.headval = tmp 

            
    # Pointer headval and p are being 
    # used here because, the headval 
    # of the linked list is changed in this function. 
    def moveToFront(self,  headval, p, m): 
        
        global first 
        global last 
        global length 
        
        # If the linked list is empty, 
        # or it contains only one node, 
        # then nothing needs to be done, simply return 
        if (headval == None): 
            return headval 
    
        p = headval 
        headval = headval.nextval
        m= m + 1
    
        # if m value reaches length, 
        # the recursion will end 
        if (length == m) : 
        
            # breaking the link 
            p.nextval = None
    
            # connecting last to first & 
            # will make another node as headval 
            last.nextval = first 
            
            # Making the first node of 
            # last m nodes as root 
            first = headval 
        
        else: 
            self.moveToFront(headval, p, m) 
          
    # UTILITY FUNCTIONS 
    
    # Function to add a node at 
    # the beginning of Linked List 
    def push(self,  head_ref, new_data): 
        
        global first 
        global last 
        global length 
        
        # allocate node 
        new_node = linkedListNode() 
        
        # put in the dataval 
        new_node.dataval = new_data 
    
        # link the old list off the new node 
        new_node.nextval = (head_ref) 
    
        # move the headval to point to the new node 
        (head_ref) = new_node 
        
        # making first & last nodes 
        if (length == 0): 
            last = head_ref 
        else: 
            first = head_ref 
    
        # increase the length 
        length= length + 1
        
        return head_ref

        
list1 = SLinkedList()
# node1 = linkedListNode("Mon")
# list1.headval = node1
# e2 = linkedListNode("Tue")
# e3 = linkedListNode("Wed")
# list1.headval.nextval = e2
# e2.nextval = e3
# list1.pushData(10)
# list1.pushData(56)
# list1.pushData(89)
# list1.AtBegining("Sun")
# list1.Inbetween(list1.headval.nextval,"Fri")
# list1.AtEnd("Thu")
# list1.RemoveNode("Tue")
# list1.removeDuplicates()
# print("track length: %i" % list1.list_length())
# print("middle element is:" + (list1.getMiddle(list1.headval).dataval)) 
# list1.printParticularItem(4)
# list1.moveItems()
  
length = 0 
start = None
start = list1.push(start, 5) 
start = list1.push(start, 4) 
start = list1.push(start, 3) 
start = list1.push(start, 2) 
start = list1.push(start, 1) 
start = list1.push(start, 0) 

# list1.moveToFront(start, None, 3) 
# list1.printList2(start)


# obj.mergeSort(obj.headval) 

class ListNode:
    def __init__(self, data):
        self.data = data       
        # store reference (next item)
        self.next = None
        # store reference (previous item)
        self.previous = None
        return

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next       
        return count

    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        
        return results
    def add_list_item(self, item):
        "add an item at the end of the list"
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        
        return
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"
        
        current_id = 1
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                # we don't have to look any further
                return
 
            # needed for the next iteration
            current_node = next_node
            current_id = current_id + 1
                
        return
# node1 = ListNode(15)
# node2 = ListNode(8.2)
# node3 = ListNode("Berlin")
# node4 = ListNode(15)
# track = DoubleLinkedList()
# print("track length: %i" % track.list_length())
# for current_node in [node1, node2, node3, node4]:
#     track.add_list_item(current_node)
#     print("track length: %i" % track.list_length())
#     track.output_list()
# results = track.unordered_search(15)
# print(results)
# track.remove_list_item_by_id(4)
# track.output_list() 
     
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