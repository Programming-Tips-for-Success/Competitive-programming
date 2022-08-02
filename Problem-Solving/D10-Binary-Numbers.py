'''
Objective
Today, we're working with binary numbers.

Task
Given a base-
integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in
's binary representation.

Sample Input 1
5

Sample Output 1
1

Sample Input 2
13

Sample Output 2
2
'''

# find which is max 0 or 1
coun=0
n = int(input())
b=str(bin(n))[2:].split('0')
print(len(max(b)))

#  bin() method returns the binary string equivalent to the given integer.
number = 5
print('The binary equivalent of 5 is:', bin(number)) # 0b101