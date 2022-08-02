

#algo

# A recursive function to find nth catalan number

def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n-i-1)

	return res


for i in range(10):
	print (catalan(i))

#other use cases Catalan no.

# Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

# Count the number of possible Binary Search Trees with n keys 

# Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

# Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.

 