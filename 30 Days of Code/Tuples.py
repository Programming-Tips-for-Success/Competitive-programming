'''
Task
Given an integer, , and space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of
.
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
Input Format
The first line contains an integer,
, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple
.
Output Format
Print the result of
.
Sample Input 0
2
1 2
Sample Output 0
3713081631934410656

'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
int_val = 4
str_val = 'samplestring'
flt_val = 24.56
print ("The integer hash value is : " + str(hash(int_val))) 
print ("The string hash value is : " + str(hash(str_val))) 
print ("The float hash value is : " + str(hash(flt_val))) 