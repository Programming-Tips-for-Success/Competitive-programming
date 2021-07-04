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

    def sortedMerge(self, a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result  



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


    def mergeSort(self, h): 
          
        # Base case if headval is None 
        if h == None or h.next == None: 
            return h 
  
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the nextval of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist

    def printList2(self, node): 
  
        while (node != None) : 
            print( node.data, end=" ") 
            node = node.next 

list1= Solution()
node1 = Node("4")
list1.headval = node1
e2 = Node("1")
e3 = Node("3")
list1.headval.next = e2
e2.next = e3

print("middle element is:" + (list1.getMiddle(list1.headval).data)) 
(list1.mergeSort(list1.headval) )
list1.printList2(list1.headval)
