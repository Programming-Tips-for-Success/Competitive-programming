# # LIS(Longest Increasing Subsequence)

# Input: arr[] = {3, 10, 2, 1, 20}
# Output: Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20

# Input: arr[] = {3, 2}
# Output: Length of LIS = 1
# The longest increasing subsequences are {3} and {2}

# Input: arr[] = {50, 3, 10, 7, 40, 80}
# Output: Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}

# // O(n^2) many variations of this problem...
#  int lengthOfLIS(vector<int>& nums) {        
#         int n = nums.size();
#         if(n==0)
#             return 0;
#         vector<int> dp(n,1);
#         int ans=1;
        
#         for(int i=1; i<n; i++){
#             for(int j=0; j<i; j++){
#                 if( nums[i] > nums[j] && dp[j]+1 > dp[i] )
#                     dp[i]=dp[j]+1;                
#             }
#             ans=max(ans, dp[i]);
#         }
#         return ans;
#     }

# Dynamic programming Python implementation
# of LIS problem

# lis returns length of the longest
# increasing subsequence in arr of size n


def lis(arr):
	n = len(arr)

	# Declare the list (array) for LIS and
	# initialize LIS values for all indexes
	lis = [1]*n

	# Compute optimized LIS values in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j]+1

	# Initialize maximum to 0 to get
	# the maximum of all LIS
	maximum = 0

	# Pick maximum of all LIS values
	for i in range(n):
		maximum = max(maximum, lis[i])

	return maximum
# end of lis function


# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))
