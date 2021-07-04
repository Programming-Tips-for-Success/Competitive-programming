'''
Objective
Today we're working with Linked Lists.

A Node class is provided for you in the editor. A Node object has an integer data field,
, and a Node instance pointer,

, pointing to another node (i.e.: the next node in a list).

A Node insert function is also declared in your editor. It has two parameters: a pointer,
, pointing to the first node of a linked list, and an integer

value that must be added to the end of the list as a new Node object.

Task
Complete the insert function in your editor so that it creates a new Node (pass
as the Node constructor argument) and inserts it at the tail of the linked list referenced by the parameter. Once the new node is added, return the reference to the

node.

Note: If the

argument passed to the insert function is null, then the initial list is empty.

Input Format

The insert function has
parameters: a pointer to a Node named , and an integer value, .
The constructor for Node has parameter: an integer value for the

field.

You do not need to read anything from stdin.

Output Format

Your insert function should return a reference to the

node of the linked list.

Sample Input

The following input is handled for you by the locked code in the editor:
The first line contains T, the number of test cases.
The

subsequent lines of test cases each contain an integer to be inserted at the list's tail.

4
2
3
4
1

Sample Output

The locked code in your editor prints the ordered data values for each element in your list as a single line of space-separated integers:

2 3 4 1

Explanation

, so the locked code in the editor will be inserting nodes.
The list is initially empty, so is null; accounting for this, our code returns a new node containing the data value as the of our list. We then create and insert nodes , , and at the tail of our list. The resulting list returned by the last call to is

, so the printed output is 2 3 4 1.

[LinkedListExplanation.png] 
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        # self.dataval = dataval
        # self.nextval = None
        # return
class Solution: 
    def __init__(self):
        self.headval = None

    def display(self,head):
        current = head
        while current is not None:
            print(current.data,end=' ')
            current = current.next

    def printList2(self, node): 
  
        while (node != None) : 
            print( node.data, end=" ") 
            node = node.next  

    def insert(self,head,data):
        new = Node(data)           
        if head==None:
            head=new
        elif head.next==None:
            head.next=new
        else:
            start=head
            while(start.next!=None):
                start=start.next
            start.next=new
        return head

    def removeDuplicates(self,head):
        current = head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def removeDuplicates2(self): 
        temp = self.headval 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data: 
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else: 
                temp = temp.next
        return self.headval   

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.headval
        self.headval = NewNode
        
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.next):
            laste = laste.next
        laste.next=NewNode  
        
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
        
    def RemoveNode(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.headval = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
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
            current_node = current_node.next
            
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
            current_node = current_node.next
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
                    previous_node.next = current_node.next
                else:
                    self.headval = current_node.next
                    # we don't have to look any further
                    return
            
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        
        return

    def printParticularItem(self, index):
             printvalue = self.headval
             i = 0
             while printvalue is not None:
                 if(i== index):
                     print(printvalue.data)
                     return
                 printvalue = printvalue.next
                 i =  i + 1

    def pushData(self, newdata):
        new_Node = Node(newdata)
        new_Node.next = self.headval
        self.headval = new_Node
        

    # move last item to first place    
    def moveItems(self):
        tmp = self.headval
        sec_last = None
        while tmp and tmp.next : 
            sec_last = tmp 
            tmp = tmp.next
  
        # point the next of the second 
        # last node to None 
        sec_last.next = None
  
        # Make the last node as the first Node 
        tmp.next = self.headval 
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
        headval = headval.next
        m= m + 1
    
        # if m value reaches length, 
        # the recursion will end 
        if (length == m) : 
        
            # breaking the link 
            p.next = None
    
            # connecting last to first & 
            # will make another node as headval 
            last.next = first 
            
            # Making the first node of 
            # last m nodes as root 
            first = headval 
        
        else: 
            self.moveToFront(headval, p, m) 
          
  
    # Function to add a node at 
    # the beginning of Linked List 
    def push(self,  head_ref, new_data): 
        global length
        global first 
        global last 
    
        
        # allocate node 
        new_node = Node() 
        
        # put in the data 
        new_node.data = new_data 
    
        # link the old list off the new node 
        new_node.next = (head_ref) 
    
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


list1= Solution()
T=int(input())
head=None

for i in range(T):
    data=int(input())

    head=list1.insert(head,data)

head=list1.removeDuplicates(head) 

list1.display(head); 


node1 = Node("Mon")
list1.headval = node1
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.next = e2
e2.next = e3
list1.pushData(10)
list1.pushData(56)
list1.pushData(89)
list1.AtBegining("Sun")
list1.Inbetween(list1.headval.next,"Fri")
list1.AtEnd("Thu")
list1.RemoveNode("Tue")
list1.removeDuplicates()
print("track length: %i" % list1.list_length())

list1.printParticularItem(4)
list1.moveItems()
  
length = 0 
start = None
start = list1.push(start, 5) 
start = list1.push(start, 4) 
start = list1.push(start, 3) 
start = list1.push(start, 2) 
start = list1.push(start, 1) 
start = list1.push(start, 0) 

list1.moveToFront(start, None, 3) 
list1.printList2(start)




