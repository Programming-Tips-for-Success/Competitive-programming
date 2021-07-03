# cycle sort
# heap sort

'''
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