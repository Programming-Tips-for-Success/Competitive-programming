# Hashing/Heap Operations
# Hashing O(1) Operation,
# Priority Queue, MaxHeap/Min Heap,
# Heapify Operation, Find Medians,
# Merge Operation in O(Logn) using Heap

# Hash tables?
# Hash Table is a data structure which stores data in an associative manner. In this, data is stored in an array format, where each data value has its own unique index value.
# Use Hash Table for quick lookups
# stores elements in key-value pairs

# In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.

# When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.

# We can resolve the hash collision using .
# Collision resolution by chaining
# Open Addressing: Linear/Quadratic Probing and Double Hashing

# Hashing is an important Data Structure that is designed to use a special function called the Hash function which is used to map a given value with a particular key for faster access of elements.

#  [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table x%10

# Collision Handling: 

# Since a hash function gets us a small number for a big key, there is the possibility that two keys result in the same value. The situation where a newly inserted key maps to an already occupied slot in the hash table is called collision and must be handled using some collision handling technique.

# Chaining: 

# The idea is to make each cell of the hash table point to a linked list of records that have the same hash function value. Chaining is simple but requires additional memory outside the table.

# Open Addressing: 

# In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL. When searching for an element, we one by one examine table slots until the desired element is found or it is clear that the element is not in the table.

# You must have a good understanding of multiple Hashing techniques 
# You should know how to analyze the probability of any Hash function and also Working knowledge of Hashing to solve geometry questions.

def hash_key( key, m):
    return key % m


m = 7

# print(f'The hash value for 3 is {hash_key(3,m)}')
# print(f'The hash value for 2 is {hash_key(2,m)}')
# print(f'The hash value for 9 is {hash_key(9,m)}')
# print(f'The hash value for 11 is {hash_key(11,m)}')
# print(f'The hash value for 7 is {hash_key(7,m)}')


hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable, 'hashTable')

removeData(123)

print(hashTable, 'after removing 123')