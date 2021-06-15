'''
The string contains only UPPERCASE characters and Print the different combinations of string on separate lines in lexicographic sorted order

Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''

from itertools import combinations
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

# s = input()
# word,r = s.split()

# for i in range(1,int(r)+1):
#     for p in sorted(list(combinations(sorted(word),i))):
#         print(''.join(p))

print (list(combinations('12345',2)))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

print (list(combinations([1,1,3,3,3],4)))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]