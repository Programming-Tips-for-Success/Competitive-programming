
# left - clockwise
# arr = [3, 4, 5, 6, 7,1, 2] 
# after rotation
#  5  6  7  1  2  3  4 

# right- anti clock wise
# after rotation
#  1  2  3  4  5  6  7 

# algo discussed
# Reversal algorithm, Block swap algorithm, iterative implementation, cyclically rotate an array by one, when elements are distinct another , when duplicates are allowed
class ArrayRotation:    
    def leftRotateByJuggling(self, arr, d, n): 
        d = d % n 
        g_c_d = self.gcd(d, n) 
        for i in range(g_c_d):        
            # move i-th values of blocks  
            temp = arr[i] 
            j = i 
            while 1: 
                k = j + d 
                if k >= n: 
                    k = k - n 
                if k == i: 
                    break
                arr[j] = arr[k] 
                j = k 
            arr[j] = temp                
            
    def gcd(self, a, b): 
        if b == 0: 
            return a 
        else: 
            return self.gcd(b, a % b)
    def rverseArray(self, arr, start, end): 
        while (start < end): 
            temp = arr[start] 
            arr[start] = arr[end] 
            arr[end] = temp 
            start += 1
            end = end-1
    def leftRotatebyReversalAlgo(self, arr, d):   
        if d == 0: 
            return
        n = len(arr) 
        self.rverseArray(arr, 0, d-1) 
        self.rverseArray(arr, d, n-1) 
        self.rverseArray(arr, 0, n-1)
    def leftRotateRec(self, arr, i, d, n):
        # Return If number of elements to be rotated is zero or equal to array size
        if (d == 0 or d == n):
            return
            # If number of elements to be rotated  is exactly half of array size
        if (n - d == d):
            self.swap(arr, i, n - d + i, d)
            return
        # ''' If A is shorter '''
        if (d < n - d):
            self.swap(arr, i, n - d + i, d)
            self.leftRotateRec(arr, i, d, n - d)
            ''' If B is shorter '''
        else:
            self.swap(arr, i, d, n - d)            
            ''' This is tricky '''
            self.leftRotateRec(arr, n - d + i, 2 * d - n, d) 

    def swap(self, arr, fi, si, d):
        #     This function swaps d elements starting at 
        #  index fi with d elements starting at index si
        for i in range(d):
            temp = arr[fi + i]
            arr[fi + i] = arr[si + i]
            arr[si + i] = temp
    def leftRotatebyIterative(self, arr, d, n): 
        if(d == 0 or d == n): 
            return 
        i = d 
        j = n - d 
        while (i != j): 
            
            if(i < j): # A is shorter
                self.swap(arr, d - i, d + j - i, i) 
                j -= i 
            
            else: # B is shorter
                self.swap(arr, d - i, d, j) 
                i -= j 
        
        self.swap(arr, d - i, d, i)
    def cyclicrotate(self, arr, n): 
        x = arr[n - 1] 
        
        for i in range(n - 1, 0, -1): 
            arr[i] = arr[i - 1] 
            
        arr[0] = x 
    
    def pairInSortedRotated(self, arr, n, x ): 
      
        # Find the pivot element 
        for i in range(0, n - 1): 
            if (arr[i] > arr[i + 1]): 
                break 
                
        # l is now index of smallest element         
        l = (i + 1) % n 
        # r is now index of largest element 
        r = i      
    
        # Keep moving either l  
        # or r till they meet 
        while (l != r): 
            
            # If we find a pair with  
            # sum x, we return True 
            if (arr[l] + arr[r] == x): 
                return True 
                
            # If current pair sum is less, 
            # move to the higher sum 
            if (arr[l] + arr[r] < x): 
                l = (l + 1) % n 
            else: 
                
                # Move to the lower sum side 
                r = (n + r - 1) % n 
        
        return False  
    def pairsInSortedRotated(self, arr, n, x): 
      
        # Find the pivot element.  
        # Pivot element is largest  
        # element of array. 
        for i in range(n): 
            if arr[i] > arr[i + 1]: 
                break
        
        # l is index of 
        # smallest element. 
        l = (i + 1) % n  
        
        # r is index of  
        # largest element. 
        r = i 
        
        # Variable to store  
        # count of number 
        # of pairs. 
        cnt = 0
    
        # Find sum of pair  
        # formed by arr[l]  
        # and arr[r] and  
        # update l, r and  
        # cnt accordingly. 
        while (l != r): 
            
            # If we find a pair  
            # with sum x, then  
            # increment cnt, move  
            # l and r to next element. 
            if arr[l] + arr[r] == x: 
                cnt += 1
                
                # This condition is  
                # required to be checked,  
                # otherwise l and r will  
                # cross each other and  
                # loop will never terminate. 
                if l == (r - 1 + n) % n: 
                    return cnt 
                
                l = (l + 1) % n 
                r = (r - 1 + n) % n 
            
            # If current pair sum  
            # is less, move to  
            # the higher sum side. 
            elif arr[l] + arr[r] < x: 
                l = (l + 1) % n 
            
            # If current pair sum  
            # is greater, move to  
            # the lower sum side. 
            else: 
                r = (n + r - 1) % n 
        
        return cnt 
    def maxSum(self, arr):
        # stores sum of arr[i] 
        arrSum = 0	
        # stores sum of i*arr[i] 
        currVal = 0
        
        n = len(arr) 
        for i in range(0, n): 
            arrSum = arrSum + arr[i] 
            currVal = currVal + (i*arr[i]) 
        # initialize result 
        maxVal = currVal 
        # try all rotations one by one and find the maximum 
        # rotation sum 
        for j in range(1, n): 
            currVal = currVal + arrSum-n*arr[n-j] 
            if currVal > maxVal: 
                maxVal = currVal 
        # return result 
        return maxVal 
    def maxSum2(self, arr, n): 
  
        # Initialize result 
        res = -sys.maxsize 
    
        # Consider rotation beginning with i 
        # for all possible values of i. 
        for i in range(0, n): 
    
    
            # Initialize sum of current rotation 
            curr_sum = 0
        
            # Compute sum of all values. We don't 
            # acutally rotation the array, but  
            # compute sum by finding ndexes when  
            # arr[i] is first element 
            for j in range(0, n): 
            
                index = int((i + j)% n)  
                curr_sum += j * arr[index]  
        
    
            # Update result if required 
            res = max(res, curr_sum) 
        return res
    def maxSum3(self, arr, n): 
    
        # Compute sum of all array elements 
        cum_sum = 0
        
        for i in range(0, n): 
            cum_sum += arr[i]  
    
        # Compute sum of i * arr[i] for  
        # initial configuration. 
        curr_val = 0
        
        for i in range(0, n): 
            curr_val += i * arr[i]  
    
        # Initialize result 
        res = curr_val  
    
        # Compute values for other iterations 
        for i in range(1, n): 
        
            # Compute next value using previous 
            # value in O(1) time 
            next_val = (curr_val - (cum_sum - arr[i-1]) +
                                        arr[i-1] * (n-1)) 
    
            # Update current value 
            curr_val = next_val  
    
            # Update result if required 
            res = max(res, next_val) 
        
        return res 
    def maxSum4(self, arr, n) : 
  
        sum = 0
        pivot = self.findPivot2(arr, n) 
    
        # difference in pivot and index  
        # of last element of array  
        diff = n - 1 - pivot  
        for i in range(n) : 
            sum = sum + ((i + diff) % n) * arr[i]  
        
        return sum
        
    # function to find pivot  
    def findPivot2(self, arr, n) : 
        for i in range(n) :  
    
            if(arr[i] > arr[(i + 1) % n]) : 
                return i
    def countRotations(self, arr, n): 
  
        # We basically find index 
        # of minimum element 
        min = arr[0] 
        for i in range(0, n): 
        
            if (min > arr[i]): 
            
                min = arr[i] 
                min_index = i 
            
        return min_index
    def countRotations2(self, arr,low, high): 
  
        # This condition is needed to  
        # handle the case when array 
        # is not rotated at all 
        if (high < low): 
            return 0
    
        # If there is only one  
        # element left 
        if (high == low): 
            return low 
    
        # Find mid 
        # (low + high)/2  
        mid = low + (high - low)/2  
        mid = int(mid) 
    
        # Check if element (mid+1) is 
        # minimum element. Consider  
        # the cases like {3, 4, 5, 1, 2} 
        if (mid < high and arr[mid+1] < arr[mid]): 
            return (mid+1) 
    
        # Check if mid itself is  
        # minimum element 
        if (mid > low and arr[mid] < arr[mid - 1]): 
            return mid 
    
        # Decide whether we need to go 
        # to left half or right half 
        if (arr[high] > arr[mid]): 
            return self.countRotations2(arr, low, mid-1) 
    
        return self.countRotations2(arr, mid+1, high) 
    def preprocess(self, arr, n): 
        temp = [None] * (2 * n) 
        
        # Store arr elements at i and i + n 
        for i in range(n): 
            temp[i] = temp[i + n] = arr[i] 
        return temp 
    
    # Function to left rotate an array k times 
    def leftRotatemultiple(self, arr, n, k, temp): 
        
        # Starting position of array after k 
        # rotations in temp will be k % n 
        start = k % n 
        
        # Print array after k rotations 
        for i in range(start, start + n): 
            print(temp[i], end = " ") 
        print("")  
    def leftRotatespaceoptmimized(self, arr, n, k): 
      
        # Print array  
        # after k rotations 
        for i in range(k, k + n): 
            print(str(arr[i % n]),  
                    end = " ")      
    def splitArr(self, arr, n, k):  
        for i in range(0, k):  
            x = arr[0] 
            for j in range(0, n-1): 
                arr[j] = arr[j + 1] 
            
            arr[n-1] = x 
    def findMin(self, arr, low, high): 
        # This condition is needed to handle the case when array is not 
        # rotated at all 
        if high < low: 
            return arr[0] 
    
        # If there is only one element left 
        if high == low: 
            return arr[low] 
    
        # Find mid 
        mid = int((low + high)/2) 
    
        # Check if element (mid+1) is minimum element. Consider 
        # the cases like [3, 4, 5, 1, 2] 
        if mid < high and arr[mid+1] < arr[mid]: 
            return arr[mid+1] 
    
        # Check if mid itself is minimum element 
        if mid > low and arr[mid] < arr[mid - 1]: 
            return arr[mid] 
    
        # Decide whether we need to go to left half or right half 
        if arr[high] > arr[mid]: 
            return self.findMin(arr, low, mid-1) 
        return self.findMin(arr, mid+1, high) 
    def reverseArray(self,  arr, start, end): 
      
        while (start < end): 
            
            arr[start], arr[end] = arr[end], arr[start] 
            start = start + 1
            end = end - 1
      
  
    # Function to right rotate arr 
    # of size n by d  
    def rightRotate(self, arr, d, n): 
        
        self.reverseArray(arr, 0, n - 1) 
        self.reverseArray(arr, 0, d - 1) 
        self.reverseArray(arr, d, n - 1)
    def maxHamming(self, arr , n ): 
  
        # arr[] to brr[] two times so 
        # that we can traverse through  
        # all rotations. 
        brr = [0] * (2 * n + 1) 
        for i in range(n): 
            brr[i] = arr[i] 
        for i in range(n): 
            brr[n+i] = arr[i] 
        
        # We know hamming distance  
        # with 0 rotation would be 0. 
        maxHam = 0
        
        # We try other rotations one by 
        # one and compute Hamming  
        # distance of every rotation 
        for i in range(1, n): 
            currHam = 0
            k = 0
            for j in range(i, i + n): 
                if brr[j] != arr[k]: 
                    currHam += 1
                    k = k + 1
            
            # We can never get more than n. 
            if currHam == n: 
                return n 
            
            maxHam = max(maxHam, currHam) 
        
        return maxHam  
 
    # Function to left rotate arr[] of size n by d*/ 
    def leftRotate(self, arr, d, n): 
        for i in range(d): 
            self.leftRotatebyOne(arr, n) 
    
    # Function to left Rotate arr[] of size n by 1*/  
    def leftRotatebyOne(self, arr, n): 
        temp = arr[0] 
        for i in range(n-1): 
            arr[i] = arr[i + 1] 
        arr[n-1] = temp 
            
    
    # utility function to print an array */ 
    def printArray(self, arr, size): 
        for i in range(size): 
            print ("% d"% arr[i], end =" ")

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return 0

        for j in range(k): 
            temp = nums[-1] 
            for i in reversed(range((n-1))):
                nums[i+1] = nums[i] 
            nums[0] = temp

        return nums

    def rightrotate(self, nums, k: int):
        k %= len(nums)
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
        return nums

    # best for big arrays
    def rotate2(self, nums, k: int):
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1
        return nums




arrayObj = ArrayRotation()
arr = [3, 4, 5, 6, 7,1, 2] 
# use temp array, Rotate one by one, Juggling Algorithm (use gcd) 
# (arrayObj.leftRotateByJuggling(arr, 2, 7) )
# arrayObj.printArray(arr, 7)  

# (arrayObj.leftRotatebyReversalAlgo(arr, 2) )
# arrayObj.printArray(arr, 7) 

# arrayObj.leftRotateRec(arr, 0, 2, 7) 
# arrayObj.printArray(arr, 7) 

# arrayObj.leftRotatebyIterative(arr, 2, 7) 
# arrayObj.printArray(arr, 7) 

# right rotate
# arrayObj.cyclicrotate(arr, 7) 
# arrayObj.printArray(arr, 7) #  2  3  4  5  6  7  1

# check if there is a pair with a given sum
# print(arrayObj.pairInSortedRotated(arr, 7,8))

# count all pairs having sum x
# print(arrayObj.pairsInSortedRotated(arr, 6,9))

arr3 = [8, 3, 1, 2]
#  all the rotations,
    # {8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
    # {3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
    # {1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
    # {2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*1 = 17
# print ("maximum value of Sum( i*arr[i]) with only rotations on given array allowed Max sum is: ", arrayObj.maxSum(arr3) )
# print (arrayObj.maxSum2(arr3, 4) )
# print (arrayObj.maxSum3(arr3, 4) )
# print('The pivot method can only be used in the case of a sorted or a rotated sorted array so maxsum is', arrayObj.maxSum4(arr3, 4))

# print('using linear search',arrayObj.countRotations(arr, 7)) 

# print('using binary search',arrayObj.countRotations2(arr, 0, 6)) 

# efficient approach to rotate multiple arrays . To handle multiple queries of array rotation, we use a temp array of size 2n and quickly handle rotations.
# temp = arrayObj.preprocess(arr, 7)
# print('multiple array rotate',arrayObj.leftRotatemultiple(arr, 7, 2, temp)) 
# print('multiple array rotate',arrayObj.leftRotatemultiple(arr, 7, 3, temp)) 
# print('multiple array rotate',arrayObj.leftRotatemultiple(arr, 7, 4, temp)) 

# optimized version of preprocess approach
# arrayObj.leftRotatespaceoptmimized(arr, 7, 2) 

# left rotate - split array and move first part to end.
# arrayObj.splitArr(arr, 7, 2) 

# print("The minimum element is " + str(arrayObj.findMin(arr, 0, 6))) 

# arrayObj.rightRotate(arr, 2, 7)
# arrayObj.printArray(arr, 7) 

# hamming is number of positions at which the corresponding character(elements) are different.
# print(arrayObj.maxHamming(arr, 6))

# arrayObj.leftRotate(arr, 2, 7) 
# arrayObj.printArray(arr, 7) 

# print(arrayObj.rotate(arr, 2)) 

# print(arrayObj.rightrotate(arr, 2)) 

# print(arrayObj.rotate2(arr, 3)) 



# reversed usage
for i in reversed(range(1, 10, 2)): 
   print(i) 

