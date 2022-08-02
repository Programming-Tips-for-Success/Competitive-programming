
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