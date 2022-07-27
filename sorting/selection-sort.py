
def Selection(arr): 

    n = len(arr)
    for i in range(n): 
        min_index = i 
        min_str = arr[i] 
        
        # Find the minimum element in unsorted subarray 
        for j in range(i+1,n): 
            if min_str>arr[j]: 
                min_str = arr[j] 
                min_index = j 
                
        # Swap the found minimum element with the first element        
        if min_index != i: 
            temp = arr[i] 
            arr[i] = arr[min_index] 
            arr[min_index] = temp 
    return arr 

arr = ['paper',  'true',  'soap',  'floppy', 'flower']
arr2 = [34, 45, 3, 5, 6]
data = Selection(arr2) 
print(data)