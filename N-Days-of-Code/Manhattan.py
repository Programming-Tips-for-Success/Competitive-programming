
# Input : n = 4
#         point1 = { -1, 5 }
#         point2 = { 1, 6 }
#         point3 = { 3, 5 }
#         point4 = { 2, 3 }
# Output : 22
# Distance of { 1, 6 }, { 3, 5 }, { 2, 3 } from 
# { -1, 5 } are 3, 4, 5 respectively.
# Therefore, sum = 3 + 4 + 5 = 12

# Distance of { 3, 5 }, { 2, 3 } from { 1, 6 } 
# are 3, 4 respectively.
# Therefore, sum = 12 + 3 + 4 = 19

# Distance of { 2, 3 } from { 3, 5 } is 3.
# Therefore, sum = 19 + 3 = 22.

# Python3 code to find sum of Manhattan
# distances between all the pairs of
# given points
 
# Return the sum of distance of one axis.
def distancesum (arr, n):
     
    # sorting the array.
    arr.sort()
     
    # for each point, finding
    # the distance.
    res = 0
    sum = 0
    for i in range(n):
        res += (arr[i] * i - sum)
        sum += arr[i]
     
    return res
     
def totaldistancesum( x , y , n ):
    return distancesum(x, n) + distancesum(y, n)
     
# Driven Code
x = [ -1, 1, 3, 2 ]
y = [ 5, 6, 5, 3 ]
n = len(x)
print(totaldistancesum(x, y, n) )