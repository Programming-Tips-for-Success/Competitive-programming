'''
Objective
Today, we're discussing a simple sorting algorithm called Bubble Sort. Check out the Tutorial tab for learning materials and an instructional video!
Consider the following version of Bubble Sort:
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
Task
Given an array,
, of size distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following
lines:
    Array is sorted in numSwaps swaps.
    where 
is the number of swaps that took place.
First Element: firstElement
where
is the first element in the sorted array.
Last Element: lastElement
where
    is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.
Input Format
The first line contains an integer,
, denoting the number of elements in array .
The second line contains space-separated integers describing the respective values of
.
Constraints
, where
    .
Output Format
Print the following three lines of output:
    Array is sorted in numSwaps swaps.
    where 
is the number of swaps that took place.
First Element: firstElement
where
is the first element in the sorted array.
Last Element: lastElement
where
    is the last element in the sorted array.
Sample Input 0
3
1 2 3
Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Explanation 0
The array is already sorted, so
swaps take place and we print the necessary
lines of output shown above.
Sample Input 1
3
3 2 1
Sample Output 1
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
Explanation 1
The array
is not sorted, so we perform the following
swaps:
At this point the array is sorted and we print the necessary lines of output shown above.
'''

# Bubble sort
# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# numberOfSwaps = 0
# for i in range(n):
#     for j in range(n-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#             numberOfSwaps += 1
#     if numberOfSwaps == 0:
#         break
# print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(numberOfSwaps,a[0],a[-1]))

# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
  
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i])

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.

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

# arr = ['paper',  'true',  'soap',  'floppy', 'flower']
# arr2 = [34, 45, 3, 5, 6]
# data = Selection(arr2) 
# print(data)

# Radix sort-  grouping the individual digits of the same place value then sort it
# also known as counting sort
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


# data = [121, 432, 564, 23, 1, 45, 788]
# radixSort(data)
# print(data)

# time complexity is O(d(n+k)) d is the number cycle and O(n+k) is the time complexity of counting sort.
# If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in linear time however the intermediate sort takes large space.
# This makes radix sort space inefficient.

# bucket sort
# dividing the elements into several groups called buckets.
def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


# array = [.42, .32, .33, .52, .37, .47, .51]
# print("Sorted Array in descending order is")
# print(bucketSort(array))

# Quick sort
# use Divide and conquer approach. Quicksort splits the array into smaller arrays until it ends up with an empty array or one that has only one element, before recursively sorting the larger arrays.

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

# comparison merge and quick sort
# Mergesort is more efficient & faster than Quicksort in case of a large array and Quicksort is more efficient & faster than Mergesort in case of a small array but memory requirement is more in mergesort as compared to quicksort.


# Both Merge sort and Insertion sort can be used for linked lists.  
# The slow random-access performance of a linked list makes other algorithms (such as quicksort)  perform poorly, and others (such as heapsort) completely impossible.  

# Since the worst-case time complexity of Merge Sort is O(nLogn) and  

# Insertion sort is O(n^2), merge sort is preferred. 