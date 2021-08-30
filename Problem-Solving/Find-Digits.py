# problem
# An integer d is a divisor of an integer n if the remainder of n/d = 0.

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.
# n=124
# Example

# Check whether 1,2  and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.

# Sample Input

# 2
# 12
# 1012

# Sample Output

# 2
# 3

# algo
# r
# 124%10 = 4  12//10 = 1
# 124 % 4 = 0
# counter ++
# 124//10 = 12
def findDigits():
    n=input()
    for i in range(int(n)):
        p = int(input())
        r = p
        count = 0
        while(r > 0):
            if (r % 10 != 0 and p % (r % 10) == 0):
                count = count + 1
            r = r // 10
        print(count)

        

findDigits()