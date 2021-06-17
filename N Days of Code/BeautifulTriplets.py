# problem statement
# Given a sequence of integers , a triplet is beautiful if Given an increasing sequence of integers and the value of  count the number of beautiful triplets in the sequence.

# Sample Input
# 7 3
# 1 2 4 5 7 8 10

# Sample Output
# 3
# (1, 4, 7) (4, 7, 10) (2, 5, 8) triplets

# code
def beautifulTriplets(d, arr):
    trip=0
    for i in arr:
        if (i+d) in arr and (i+2*d) in arr:
            trip+=1
    return trip

# nd = input().split()
# n = int(nd[0])
n = 7
# d = int(nd[1])
d = 3
# arr = list(map(int, input().rstrip().split()))
arr = [1, 2, 4, 5, 7, 8, 10]
result = beautifulTriplets(d, arr)
print(result)


