# Primality Testing Algorithms
# Sieve Of Eratosthenes, 
# Fermat primality test and Miller–Rabin primality test (both are nondeterministic)
# Both of these are compositeness tests. If a number is proved to be composite, then it sure isn’t a prime number. Miller-Rabin is a more sophisticated one than Fermat’s. Infact, Miller-Rabin also has a deterministic variant, but then its a game of trade between time complexity and accuracy of the algorithm.

# Application:

# The single most important use of prime numbers is in Cryptography. More precisely, they are used in encryption and decryption in RSA algorithm which was the very first implementation of Public Key Cryptosystems
# Another use is in Hash functions used in Hash Tables
'''
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!
Task
A prime is a natural number greater than
that has no positive divisors other than and itself. Given a number, , determine and print whether it's or
.
Note: If possible, try to come up with a
primality algorithm, or see what sort of optimizations you come up with for an
algorithm. Be sure to check out the Editorial after submitting your code!
Input Format
The first line contains an integer,
, the number of test cases.
Each of the subsequent lines contains an integer,
, to be tested for primality.
Constraints
Output Format
For each test case, print whether
is or
on a new line.
Sample Input
3
12
5
7
Sample Output
Not prime
Prime
Prime
Explanation
Test Case 0:
.
is divisible by numbers other than and itself (i.e.: , , ), so we print
on a new line.
Test Case 1:
.
is only divisible and itself, so we print
on a new line.
Test Case 2:
.
is only divisible and itself, so we print on a new line.
'''
import math
nums=list()
def checkPrime():
    n = int(input())
    for i in range(n):
        nums.append(int(input()))
for _ in nums:
    if _ == 1 or _ == 0:
        print('Not prime')
    else:
        m=0
        for a in range(2,int(math.sqrt(_))+1):
            if _%a == 0:
                m+=1
        if m == 0:
            print('Prime')
        else:
            print('Not prime')

def isPrime(n): 
   if(n<=1): 
       return False 
   for i in range(2, n): 
        if(n%i==0): 
            return False 
        return True  

# The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n.
# Sieve of Eratosthenes (deterministic)

# If we have certain limit on the range of numbers, say determine all primes within range 100 to 1000 then Sieve is a way to go. The length of range is a crucial factor, because we have to allocate certain amount of memory according to rang
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            print (p, end= " ")

SieveOfEratosthenes(10)

#   Find the sum of all the prime numbers less than 1000 that are 1 more than a perfect square.

def SieveOfEratosthenes2(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    sum = 0
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]:
            sum = sum + p 
            root = math.sqrt(p)
            if root*root == p:
                print('perfect', p, root)
    print(sum, 'sum')
            
SieveOfEratosthenes2(20)

#   Return the next higher prime number

def prime(n):
    next_prime = n + 1
    prime = True
    while True:
        for i in range(2, next_prime):
            if next_prime%i ==0:
                prime = False
                break
        if prime:
            return next_prime
        else:
            next_prime = next_prime + 1
            if next_prime % 2 == 0:
                next_prime = next_prime + 1
            prime = True

print(prime(5))

#  printing prime numbers in one thread and non primes in another thread,
