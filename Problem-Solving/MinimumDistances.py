'''
We define the distance between two array values as the number of indices between the two values. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, print -1

Sample Input

6
7 1 3 4 1 7

Sample Output

3
'''

# explanation
# two pairs 1 7
# 7 index = 0, 5
# 1 index = 1, 4
# distance = 3

# Complete the minimumDistances function below.
def minimumDistances(a):
    dis=2000
    for l in range(len(a)):
        try:
            u=a.index(a[l],l+1,len(a)) 
            dis=min(dis,u-l)
        except:
            pass
        
    if dis==2000:
        return -1
    return dis


n = int(input())

a = list(map(int, input().rstrip().split()))

result = minimumDistances(a)

print(str(result) + '\n')
