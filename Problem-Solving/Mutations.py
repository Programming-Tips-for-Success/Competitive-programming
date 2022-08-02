'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Task
Read a given string, change the character at a given index and then print the modified string.

Input Format
The first line contains a string,
.
The next line contains an integer , denoting the index location and a character

separated by a space.

Output Format
Using any of the methods explained above, replace the character at index
with character

.

Sample Input

abracadabra
5 k

Sample Output

abrackdabra

'''

def mutate_string(string, position, character):
    stl=list(string)
    stl[position]=character
    return ''.join(stl)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)