# problem statement
# Given a sequence of integers , a triplet is beautiful if Given an increasing sequence of integers and the value of  count the number of beautiful triplets in the sequence.

# Sample Input
# 7 3
#           1 2 4 5 7 8 10
# indices - 0 1 2 3 4 5 6
# Sample Output
# 3  triplets - (1, 4, 7) (2, 5, 8) (4, 7, 10) 

# 5 2
# 1 2 1 2 4

# algo
# first iteration - 1
# 4  in arr and 7 in arr

# second iteration - 2
# 5 in arr and 8 in arr

# third iteration - 4
# 7 in arr and 10 in arr

# fourth- 5
# 8 in arr and 11 is not in arr

# code
def beautifulTriplets(d, arr):
    trip=0
    for i in arr:
        if (i+d) in arr and (i+2*d) in arr:
            trip+=1
    return trip

nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
result = beautifulTriplets(d, arr)
print(result)




