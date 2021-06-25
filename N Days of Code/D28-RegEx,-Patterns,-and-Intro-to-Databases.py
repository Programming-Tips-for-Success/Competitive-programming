'''
Objective
Today, we're working with regular expressions. Check out the Tutorial tab for learning materials and an instructional video!
Task
Consider a database table, Emails, which has the attributes First Name and Email ID. Given
rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in
.
Input Format
The first line contains an integer,
, total number of rows in the table.
Each of the subsequent lines contains
space-separated strings denoting a person's first name and email ID, respectively.
Constraints
Each of the first names consists of lower case letters
only.
Each of the email IDs consists of lower case letters
, and
    only.
    The length of the first name is no longer than 20.
    The length of the email ID is no longer than 50.
Output Format
Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.
Sample Input
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
Sample Output
julia
julia
riya
samantha
tanya
'''
import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     N = int(input())
#     det=dict()
#     for N_itr in range(N):
#         firstNameEmailID = input().split()
#         firstName = firstNameEmailID[0]
#         emailID = firstNameEmailID[1]
#         if emailID.endswith('@gmail.com'):
#             det[emailID] = firstName
# for _ in sorted(det.values()):
#     print(_)

# "abc*" matches "ab" followed by zero or more occurances of "c", for example,
# "ab", "abc", "abcc", etc.
# "abc+" matches "ab" followed by one or more occurances of "c", for example,
# "abc", "abcc", etc, but not "ab".
# "abc?" matches "ab" followed by zero or one occurances of "c", for example, "ab" or "abc".
# Alternate patterns (separated by a vertical bar) match either of the alternative 
# patterns. For example, "(aaa)|(bbb)" will match either "aaa" or "bbb".
#  a set matches any character in the set or range. For example, "[abc]" 
# matches "a" or "b" or "c". And, for example, "[_a-­z0­-9]" matches an underscore or any lower­case letter or any digit
# () - concat data

# "ab(cd)*ef" is a pattern that matches "ab" followed by any number of occurances of "cd" 
# followed by "ef", for example, "abef", "abcdef", "abcdcdef", etc

# "\d" (any digit), "\w" (any alphanumeric character), "\W" (any non­alphanumeric character)

def testPattern():
    pat = re.compile('aa[bc]*dd')

    while 1:
        line = input('Enter a line ("q" to quit):')
        if line == 'q':
            break
        if pat.search(line):
            print( 'matched:', line)
        else:
            print ('no match:', line)

pat = re.compile('aa[0-­9]*bb')

# Use match() to match at the beginning of a string (or not at all).
# Use search() to search a string and match the first string from the left
# When a match or search is successful, it returns a match object. When it fails, it 
# returns None
x = pat.match('aa1234bbccddee')
print(x, '')

x = pat.match('xxxxaa1234bbccddee')
print(x)

x = pat.search('xxxxaa1234bbccddee')
print(x)

x = re.search(pat, 'xxxxaa1234bbccddee')
print(x)

# Write a function that can accept a regex like “*t*e*s*t*”.