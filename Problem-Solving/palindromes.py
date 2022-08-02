# problem statement
# Can you determine if a given string, is a palindrome?



# Sample Input
# racecar

# Sample Output
# The word, racecar, is a palindrome.

# Algorithm
# To solve this challenge, we must first take each character in
# , enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means
# isn't a palindrome).

# A void pushCharacter(char ch) method that pushes a character onto a stack.
# A void enqueueCharacter(char ch) method that enqueues a character in the instance variable.
# A char popCharacter() method that pops and returns the character at the top of the instance variable.
# A char dequeueCharacter() method that dequeues and returns the first character in the instance variable.


class Solution:
    def __init__(self):
        self.stack=list()
        self.queue=list()
    
    def pushCharacter(self, ch):
        self.stack.append(ch)
    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, ch):
        self.queue.append(ch)
    def dequeueCharacter(self):
        return self.queue.pop(0)

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   
l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 

# problem statement
# From the given list of integers, write down a program to identify the integers that are palindromes

l = input("Enter a list of numbers : ").split()
for num in l:
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            break
    else:
        print(num, "is a palindrome")