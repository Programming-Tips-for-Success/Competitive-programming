'''
column * row
Objective
Today, we're building on our knowledge of Arrays by adding another dimension. 
Context
Given a
2D Array,
:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in
to be a subset of values with indices falling in this pattern in
's graphical representation:
a b c
  d
e f g
There are
hourglasses in
, and an hourglass sum is the sum of an hourglass' values.
Task
Calculate the hourglass sum for every hourglass in
, then print the maximum hourglass sum.
Input Format
There are
lines of input, where each line contains space-separated integers describing 2D Array ; every value in will be in the inclusive range of to
.
Constraints
Output Format
Print the largest (maximum) hourglass sum found in
.
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19
Explanation
contains the following hourglasses:
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0
0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0
1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0
0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum (
) is:
2 4 4
  2
1 2 4
'''

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
sums = []
for i in range(len(arr) - 2):
    for j in range(len(arr[i]) - 2):
        val = 0
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                if row == i or row == i + 2:
                    val += arr[row][col]
                elif row == i + 1 and col == j + 1:
                    val += arr[row][col]
        sums.append(val)
print(max(sums))
 

def createEmptyMatrix(n):
    arr = []
    for i in range(n):
        nestedArr = []
        for j in range(n):
            nestedArr.append(0)
        arr.append(nestedArr)

    for i in (arr):
        print(i)

createEmptyMatrix(3)

def initializeMatrix(m, n):
    a = [[0 for i in range(n)] for j in range(m)]
    print(a)

initializeMatrix(2, 3)

# add two matrix-
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# multiplication of matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)


def printMatrix(m, n):
    m = int(input('enter rows'))
    n = int(input('columns'))
    mat = []

    for i in (range(m)):
        sub = []
        for j in range(n):
            sub.append(int(input()))
        mat.append(sub)

    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()

printMatrix(2, 3)  


