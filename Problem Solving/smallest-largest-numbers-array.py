# Identify the smallest and largest numbers amongst the unsorted array of integers

def minMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        # if the current element is greater than the max, then set max to current element
        if arr[i] > max:
            max = arr[i]
        # if the current element is lesser than the min, then set min to current element
        if arr[i] < min:
            min = arr[i]
    print('min', min, 'max', max)

minMax([2, 4, 7, 6, 5, 1, 3, 10])
