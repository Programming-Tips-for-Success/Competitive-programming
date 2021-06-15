# Write down a program to identify duplicates in an array of integers.

def findDuplicates(arr):
    for i in range(0, len(arr)):  
        for j in range(i+1, len(arr)):  
            if(arr[i] == arr[j]):  
                print(arr[j]); 

findDuplicates([1, 2, 3, 4, 2, 7, 8, 8, 3]) 