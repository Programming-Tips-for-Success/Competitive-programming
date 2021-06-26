# topics to cover
# Iterative & recursive approaches
# Doubly LinkedList, flattering linked list
# Sorting and searching operations on LL

# The following operations make linked lists an ADT:
# Main Linked Lists Operations
#  Insert: inserts an element into the list
#  Delete: removes and returns the specified position element from the list

# Auxiliary Linked Lists Operations
#  Delete List: removes all elements of the list (disposes the list)
#  Count: returns the number of elements in the list
#  Find 𝑛𝑡ℎ node from the end of the list

# Implement Stack using Linked List
# You are given a pointer to the first element of a linked list 𝐿. There are two possibilities for 𝐿, it
# either ends (snake) or its last element points back to one of the earlier elements in the list (snail). Task is to
# devise an algorithm that tests whether a given list 𝐿 is a snake or a snail.

# Check whether the given linked list is either NULL-terminated or not. If there is a cycle find the
# start node of the loop.

# Insert a node in a sorted linked list

# Reverse a singly linked list

# How will you find the middle of the linked list?

#  How will you display a linked list from the end?

# Check whether the given Linked List length is even or odd?

# If the head of a linked list is pointing to 𝑘𝑡ℎ element, then how will you get the elements before
# 𝑘𝑡ℎ element

# Given two sorted Linked Lists, we need to merge them into the third list in sorted order. 

# Reverse the linked list in pairs. If you have a linked list that holds 1→2→3→4→𝑋, then after the
# function has been called the linked list would hold 2→1→4→3→X

# Given a binary tree convert it to doubly linked list.

# How do we sort the Linked Lists?

# Split a Circular Linked List into two equal parts. If the number of nodes in the list are odd then
# make first list one node extra than second list.

# How will you check if the linked list is palindrome or not?

# Exchange the adjacent elements in a link list.

# For a given 𝐾 value (𝐾 > 0) reverse blocks of 𝐾 nodes in a list.
# Example: Input: 1 2 3 4 5 6 7 8 9 10, 
# Output for different 𝐾 values:
# For 𝐾 = 2: 2 1 4 3 6 5 8 7 10 9, For 𝐾 = 3: 3 2 1 6 5 4 9 8 7 10, For 𝐾 = 4: 4 3 2 1 8 7 6 5 9 10

# JosephusCircle: 𝑁 people have decided to elect a leader by arranging themselves in a circle
# and eliminating every 𝑀𝑡ℎ person around the circle, closing ranks as each person drops out. Find which
# person will be the last one remaining (with rank 1)

# Find modular node: Given a singly linked list, write a function to find the last element from the
# beginning whose 𝑛%𝑘 == 0, where 𝑛 is the number of elements in the list and 𝑘 is an integer constant. For
# example, if 𝑛 = 19 and 𝑘 = 3 then we should return 18𝑡ℎnode

# Find modular node from end: Given a singly linked list, write a function to find the first
# element from the end whose 𝑛%𝑘 == 0, where 𝑛 is the number of elements in the list and 𝑘 is an integer
# constant. For example, if 𝑛 = 19 and 𝑘 = 3 then we should return 16𝑡ℎnode.

# Find fractional node: Given a singly linked list, write a function to find the 𝑛/𝑘 𝑡ℎ element, where
# 𝑛 is the number of elements in the list.

# Median in an infinite series of integers- 
# : Median is the middle number in a sorted list of numbers (if we have odd number of elements). If we
# have even number of elements, median is the average of two middle numbers in a sorted list of numbers.
# We can solve this problem with linked lists (with both sorted and unsorted linked lists)


# Given a singly linked list L: 𝐿1-> 𝐿2-> 𝐿3…-> 𝐿𝑛−1-> 𝐿𝑛, reorder it to: 𝐿1-> 𝐿𝑛-> 𝐿2-> 𝐿𝑛−1……
#  We divide the list in two parts for instance 1->2->3->4->5 will become 1->2->3 and 4->5, we have to
# reverse the second list and give a list that alternates both


# Which sorting algorithm is easily adaptable to singly linked lists?
# Solution: Simple Insertion sort is easily adabtable to singly linked list. To insert the an element, the linked list
# is traversed until the proper position is found, or until the end of the list is reached. It be inserted into the list
# by merely adjusting the pointers without shifting any elements unlike in the array. This reduces the time
# required for insertion but not the time required for searching for the proper position

# How do you implement insertion sort for linked lists?

# Given a list, rotate the list to the right by k places, where k is non-negative. For example: Given
# 1->2->3->4->5->NULL and k = 2, return 4->5->1->2->3->NULL.

# You are given two linked lists representing two non-negative numbers. The digits are stored in
# reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked
# list. For example with input: (3 -> 4 -> 3) + (5 -> 6 -> 4); the output should be 8 -> 0 -> 8.

# Given a linked list and a value K, partition it such that all nodes less than K come before nodes
# greater than or equal to K. You should preserve the original relative order of the nodes in each of the two
# partitions. For example, given 1->4->3->2->5->2 and K = 3, return 1->2->2->4->3->5.

# Merge k sorted linked lists and return it as one sorted list.
# you can use priority queue here

# Given a unordered linked list, how do you remove duplicates in it?
'''
Objective
Today we're working with Linked Lists. Check out the Tutorial tab for learning materials and an instructional video!

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
class Solution: 
    def __init__(self):
        self.headval = None
    def display(self,head):
        current = head
        while current is not None:
            print(current.data,end=' ')
            current = current.next

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
    
    def getMiddle(self, headval): 
        if (headval == None): 
            return headval 
  
        slow = headval 
        fast = headval 
  
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
              
        return slow


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
          
    # UTILITY FUNCTIONS 
    
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

  

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)    
mylist.display(head); 

# Reverse the second half of a linked list 

# remove duplicates from an unsorted singly linked list.
# Write a program that returns the middle node of an unsorted linked list.
# Given an unsorted singly linked list and an integer index, write a program that outputs the value of the node at the designated 
# index position. 
# Given a singly linked list, write a program the shifts every node kk unit to the left.
# For example
# When 4\rightarrow→6\rightarrow→8\rightarrow→9 is shifted 2 units left it becomes 8\rightarrow→9\rightarrow→4\rightarrow→6
# Given a sorted circular linked list of Nodes that store integers and a new Node, insert the new Node into the correct position.
# For example, 2 is a prime that is 1 more than the perfect square 1.
# design the data structures for Zomato cuisines adding and removing system, different ways of designing approaches.
# finding middle element of linked list 
# Deleting the First Node in Singly Linked List
# Deleting the Last node in Singly Linked List
# Deleting Singly Linked List
