
#  Union-find set 

'''
Objective
Today, we're learning about a new data type: sets.

Concept

If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']

If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]

Sets are an unordered bag of unique values. A single set contains values of any immutable data type.

CREATING SETS

>> myset = {1, 2} # Directly assigning values to a set
>> myset = set()  # Initializing a set
>> myset = set(['a', 'b']) # Creating a set from a list
>> myset
{'a', 'b'}


MODIFYING SETS

Using the add() function:

>> myset.add('c')
>> myset
{'a', 'c', 'b'}
>> myset.add('a') # As 'a' already exists in the set, nothing happens
>> myset.add((5, 4))
>> myset
{'a', 'c', 'b', (5, 4)}


The union() and intersection() functions are symmetric methods:

>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False

These other built-in data structures in Python are also useful.

Task
Given
sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or

but do not exist in both.

Input Format

The first line of input contains an integer,
.
The second line contains space-separated integers.
The third line contains an integer, .
The fourth line contains

space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12

Sample Output

5
9
11
12

'''
if __name__=='__main__':
    n=int(input())
    a=input().split()
    m=int(input())
    b=input().split()
    a=[int(i) for i in a]
    b=[int(i) for i in b]

a=set(a)
b=set(b)
ad=a.difference(b)
bd=b.difference(a)
d=ad.union(bd)
d=list(d)
for i in sorted(d):
    print(i)

# Union of two arrays

# Arrays- A B
# size- N M

# ES6
#   let arr1 = [1,2,3,4,5,6,7];
#         let arr2 = [1,2,3,8]; 
#     let union = [...new Set([...arr1, ...arr2])];
#     console.log(union)

def doUnion(a,n,b,m):
    
    #code here
    return len(set(a+b))

def doUnion(a,n,b,m): 
    hs=set() 
    
    for i in range(0,n): 
        hs.add(a[i]) 
        
    for i in range(0,m): 
        hs.add(b[i]) 
    
    return len(hs)

# difference usage
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"]) 
print(color_list_1.difference(color_list_2)) 

# COMMON SET OPERATIONS Using union(), intersection() and difference() functions.

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b {2, 4, 5, 9, 11, 12}
a.intersection(b) # Values which exist in a and b {2, 4}
a.difference(b) # Values which exist in a but not in b {9, 5}

# Using the update() function:
myset = {1, 2}
myset.update([1, 2, 3, 4]) # update() only works for iterable objects
myset.update({1, 7, 8})
myset.update({1, 6}, [5, 13])
