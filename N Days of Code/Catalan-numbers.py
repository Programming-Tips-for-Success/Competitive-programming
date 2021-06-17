# Catalan numbers

# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

# Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
# Count the number of possible Binary Search Trees with n keys (See this)
# Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
# Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.

# The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …  

# A recursive function to
# find nth catalan number
def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum
	# of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n-i-1)

	return res


for i in range(10):
	print (catalan(i)),

 