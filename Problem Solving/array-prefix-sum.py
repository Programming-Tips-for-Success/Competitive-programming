
# prefix or presum
# Input  : arr[] = {10, 20, 10, 5, 15}
# Output : prefixSum[] = {10, 30, 40, 45, 60}

def prefix_sums(A):
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for k in range(1, n):
        P[k] = P[k - 1] + A[k]
    return P
arr = [10, 20, 10, 5, 15]
print(prefix_sums(arr))


