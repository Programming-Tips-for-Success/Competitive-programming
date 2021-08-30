# You are given a mapping like a -> 1, b-> 2… z-> 26. You have to print all possible combinations of a given number using the above information.
# Input:  digits[] = "121"
# Output: 3
# // The possible decodings are "ABA", "AU", "LA"
 
# Recursive implementation of numDecodings
def numDecodings(s: str) -> int:
	if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
		return 0
	return numDecodingsHelper(s, len(s))


def numDecodingsHelper(s: str, n: int) -> int:
	if n == 0 or n == 1:
		return 1
	count = 0
	if s[n-1] > "0":
		count = numDecodingsHelper(s, n-1)
	if (s[n - 2] == '1'
		or (s[n - 2] == '2'
			and s[n - 1] < '7')):
		count += numDecodingsHelper(s, n - 2)
	return count


digits = "121"
print("Count is ", numDecodings(digits))

# the recursive solution is similar to Fibonacci Numbers. Therefore, we can optimize the above solution to work in O(n) time using Dynamic Programming. 

# A Dynamic Programming based Python3
# implementation to count decodings

# A Dynamic Programming based function
# to count decodings
def countDecodingDP(digits, n):

	count = [0] * (n + 1) # A table to store
						# results of subproblems
	count[0] = 1
	count[1] = 1

	for i in range(2, n + 1):

		count[i] = 0

		# If the last digit is not 0, then last
		# digit must add to the number of words
		if (digits[i - 1] > '0'):
			count[i] = count[i - 1]

		# If second last digit is smaller than 2
		# and last digit is smaller than 7, then
		# last two digits form a valid character
		if (digits[i - 2] == '1' or
		(digits[i - 2] == '2' and
			digits[i - 1] < '7') ):
			count[i] += count[i - 2]

	return count[n]

# Driver Code
digits = "121"
n = len(digits)
print("Count is" ,
	countDecodingDP(digits, n))

