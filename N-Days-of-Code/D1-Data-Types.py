'''
 data types

variables: one of type int, one of type double, and one of type String.

Print the sum of both integers on the first line, the sum of both doubles (scaled to

decimal place) on the second line, and then the two concatenated strings on the third line.

Sample Input

12
4.0
is the best place to learn and practice coding!

Sample Output

16
8.0
HackerRank is the best place to learn and practice coding!

Explanation

When we sum the integers
and , we get the integer .
When we sum the floating-point numbers and , we get

.
When we concatenate HackerRank with is the best place to learn and practice coding!, we get HackerRank is the best place to learn and practice coding!.

You will not pass this challenge if you attempt to assign the Sample Case values to your variables instead of following the instructions above and reading input from stdin.
'''

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2,d2,s2=0,0,''
# Read and save an integer, double, and String to your variables.
i2=int(input())
d2=float(input())
s2=input()
# Print the sum of both integer variables on a new line.
print(i+i2)
# Print the sum of the double variables on a new line.
print(d+d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+s2)

# unsigned and signed integer