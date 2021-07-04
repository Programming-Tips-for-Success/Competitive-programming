# 1. Max product subarray.
# Input: arr[] = [9, -6, 10, 3] 
# Output: 30 
# Explanation: The subarray [10, 3] has the maximum product.
# Example 2

# Input: arr[] = [6, -3, -10, 0, 2] 
# Output: 180  
# Explanation: The subarray [6, -3, -10] has the maximum Product.
# Example 3

# Input: arr[] = [-2, -3, 0, -2, -40] 
# Output:  80  
# Explanation: The subarray [-2, -40] has the maximum product. 

# - DP: arroach.
# - there is also negetive and 0 number so we need slide variation of kadenes.
# - 2 minus number product also become big pos numer.
# - so we make 2 array 1 is maintain max product with pos number.
# - second is min product with neg number. neg smaller is same as max pos after mult.

# algo
# int max_till[n], min_till[n];
# int ans=a[0];
# max_till[0]=min_till[0]=ans;

# for(int i=1; i<n; i++){
# 	max_till[i]=max({a[i], max_till[i-1]*a[i], min_till[i-1]*a[i]});
# 	min_till[i]=min({a[i], max_till[i-1]*a[i], min_till[i-1]*a[i]});
# 	ans=max(ans, max_till[i]);
# }
# return ans;

# -- we can also resuce space here.

# Python 3 program to find maximum
# product subarray

# Function to find maximum
# product subarray
def maxProduct(arr, n):
	
	# Variables to store maximum and
	# minimum product till ith index.
	minVal = arr[0]
	maxVal = arr[0]

	maxProduct = arr[0]

	for i in range(1, n, 1):
		
		# When multiplied by -ve number,
		# maxVal becomes minVal
		# and minVal becomes maxVal.
		if (arr[i] < 0):
			temp = maxVal  
			maxVal = minVal
			minVal = temp
			
		# maxVal and minVal stores the
		# product of subarray ending at arr[i].
		maxVal = max(arr[i], maxVal * arr[i])
		minVal = min(arr[i], minVal * arr[i])

		# Max Product of array.
		maxProduct = max(maxProduct, maxVal)

	# Return maximum product
	# found in array.
	return maxProduct


# arr = [-1, -3, -10, 0, 60]
arr =  [9, -6, 10, 3] 

n = len(arr)

print("Maximum Subarray product is",
                maxProduct(arr, n))


print(max(2, 4))
print(max([2, 4, 6]))



