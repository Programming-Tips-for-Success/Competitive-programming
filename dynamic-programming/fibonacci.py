# fibonacci
def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1

    else: return fibo(n-1)+fibo(n-2)

print(fibo(8))

# using DP
# Python program for Memoized version of nth Fibonacci number

# Function to calculate nth Fibonacci number
def fib(n, lookup):

	# Base case
	if n == 0 or n == 1 :
		lookup[n] = n

	# If the value is not calculated previously then calculate it
	if lookup[n] is None:
		lookup[n] = fib(n-1 , lookup) + fib(n-2 , lookup)

	# return the value corresponding to that value of n
	return lookup[n]
# end of function

# Driver program to test the above function
def main():
	n = 8
	# Declaration of lookup table
	# Handles till n = 100
	lookup = [None]*(101)
	print ("Fibonacci Number is ", fib(n, lookup))

main()

# Python program Tabulated (bottom up) version
def fib(n):

	# array declaration
	f = [0]*(n+1)

	# base case assignment
	f[1] = 1

	# calculating the fibonacci and storing the values
	for i in range(2 , n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

# Driver program to test the above function
def usingTabulation():
	n = 8
	print ("Fibonacci number is " , fib(n))


usingTabulation()


