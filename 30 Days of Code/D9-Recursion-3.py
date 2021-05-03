'''
Objective
Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!
Recursive Method for Calculating Factorial
Task
Write a factorial function that takes a positive integer,
as a parameter and prints the result of (
factorial).
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of
.
Input Format
A single integer,
(the argument to pass to factorial).
Constraints
    Your submission must contain a recursive function named factorial.
Output Format
Print a single integer denoting
.
Sample Input
3
Sample Output
6
Explanation
Consider the following steps:
From steps and , we can say ; then when we apply the value from to step , we get . Thus, we print as our answer.
'''
import math
import os
import random
import re
import sys
# Complete the factorial function below.
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

n = int(input())
result = factorial(n)
print(result)

def factWithoutRecursion(n):
    temp = 1
    for i in range(n, 0, -1):
        temp = temp * i
    return temp
a = factWithoutRecursion(5) 


print(a) 
 # find power of any number 
def power(x, y):  
       
    if y == 0:  
        return 1 
    if y % 2 == 0:  
        return power(x, y // 2) * power(x, y // 2)  
           
    return x * power(x, y // 2) * power(x, y // 2)  
  
a = power(2, 5) 
print(a) 
 
# fibonacci
def F(n):
    if n == 0: return 0
    elif n == 1: return 1

    else: return F(n-1)+F(n-2)

# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number
# that divides both of them. 
# For example GCD of 20 and 28 is 4
# 20 = 2 *2 * 5
# 28 = 2 * 2*7 


def gcd(a,b):
     
    # Everything divides 0 
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
a = 20
b = 28
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:

    print('not found')