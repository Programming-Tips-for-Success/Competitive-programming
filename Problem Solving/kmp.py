 


# Knuth-Morris-Pratt String Matching (KMP)
# Knuth-Morris-Pratt algorithm  used  for finding sub string.
# in this we reduce the iteration on pattern.
# complexity  O(n+m)
# Knuth-Morris-Pratt algorithm or Boyer-Moore String Search algorithm is faster single pattern string searching algorithm, than Rabin-Karp

# Initialise array based on the failure function:
def init_arr(w):
    m = len(w)
    i = 0
    j = 1

    # No proper prefix for string of length 1:
    global arr
    arr[0] = 0

    while j < m:
        if w[i] == w[j]:
            i += 1
            arr[j] = i
            j += 1

        # The first character didn't match:
        elif i == 0:
            arr[j] = 0
            j += 1

        # Mismatch after at least one matching character:
        else:
            i = arr[i - 1]


def kmp_search(w, s):
    # Initialise array:
    init_arr(w)

    # Initialising variables:
    i = 0
    j = 0
    m = len(w)
    n = len(s)

    # Start search:
    while i < m and j < n:
        # Last character matches -> Substring found:
        if w[i] == s[j] and i == m - 1:
            return True

        # Character matches:
        elif w[i] == s[j]:
            i += 1
            j += 1

        # Character didn't match -> Backtrack:
        else:
            if i != 0:
                i = arr[i-1] 
            else:
                j += 1

    # Substring not found:
    return False

text = "hayhello"
substring = "lo"
arr = [None] * len(substring)

if kmp_search(substring, text):
    print("Substring found!")
else:
    print("Could not find substring.")
