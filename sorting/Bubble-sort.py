# Bubble sort
# for (int i = 0; i < n; i++) {
#     // Track number of elements swapped during a single array traversal
#     int numberOfSwaps = 0;
    
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#             numberOfSwaps++;
#         }
#     }
    
#     // If no elements were swapped during a traversal, array is sorted
#     if (numberOfSwaps == 0) {
#         break;
#     }
# }

# sample input
# 4
# 2 3 1 4

# sample output
# Array is sorted in 2 swaps.
# First Element: 1
# Last Element: 4

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(numberOfSwaps,a[0],a[-1]))

