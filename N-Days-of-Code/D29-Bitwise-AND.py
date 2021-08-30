# The & (bitwise AND) The result of AND is 1 only if both bits are 1.
# The | (bitwise OR)  The result of OR is 1 if any of the two bits is 1.
# The ^ (bitwise XOR) The result of XOR is 1 if the two bits are different.
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 0 ^ 0 = 0
# The << (left shift)  left shifts the bits of the first operand, the second operand decides the number of places to shift.
# The >> (right shift)  right shifts the bits of the first operand, the second operand decides the number of places to shift.
# The ~ (bitwise NOT) takes one number and inverts all bits of it
#       8421
# 5(00000101)
# 2(00000010)
# 8(00001000)

# Bit magic
# https://www.geeksforgeeks.org/bitwise-algorithms/
'''
bitwise operations

problem - Find two integers, and (where ), from set such that the value of is the maximum possible and also less than a given integer.

set = {1, 2, 3, ..n}

input
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

Sample Input

3
5 2
8 5
2 2

Sample Output

1  
4
0

maximum possible values
'''



def maxbit(n, k):
    m = 0

    for i in range(1, n + 1):
        for j in range(1, i):
            x = i & j
            if (m < x < k):
                m = x
                if (m == (k - 1)):
                    return m
    return m

t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    print(maxbit(n, k))