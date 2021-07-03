
class linkedListNode:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        return

class Merge():
# Merge sort
# It is one of the most famous divide-and-conquer sorting algorithms. This algorithm can be used to sort values in any traversable data structure (i.e., a linked list).
    def __init__(self):
        self.headval = None

        
    
    def mergeSort(self, array):
        if len(array) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(array)//2
            L = array[:r]
            M = array[r:]

            # Sort the two halves
            self.mergeSort(L)
            self.mergeSort(M)

            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1


    # Print the array
    def printList(self,array):
        for i in range(len(array)):
            print(array[i], end=" ")
        print()

# merge sort using LL
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

    # def mergeSort(self, h): 
            
    #     # Base case if headval is None 
    #     if h == None or h.next == None: 
    #         return h 

    #     # get the middle of the list  
    #     middle = self.getMiddle(h) 
    #     nexttomiddle = middle.next

    #     # set the next of middle node to None 
    #     middle.next = None

    #     # Apply mergeSort on left list  
    #     left = self.mergeSort(h) 
            
    #     # Apply mergeSort on right list 
    #     right = self.mergeSort(nexttomiddle) 

    #     # Merge the left and right lists  
    #     sortedlist = self.sortedMerge(left, right) 
    #     return sortedlist
    # def listprint(self):
    #     printval = self.headval
    #     while printval is not None:
    #         print (printval.data)
    #         printval = printval.next

a = Merge()

array = [6, 5, 12, 10, 9, 1]
a.mergeSort(array)
print("Sorted array is: ")
a.printList(array)

node1 = linkedListNode("3")
a.headval = node1
e2 = linkedListNode("1")
e3 = linkedListNode("2")
a.headval.next = e2
e2.next = e3
(a.mergeSort(a.headval))
a.listprint()


