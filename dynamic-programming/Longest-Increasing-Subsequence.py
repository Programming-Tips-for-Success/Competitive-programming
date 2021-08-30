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

#algo
# arr = [10, 22, 9, 33, 21, 50, 41, 60]
# find length
# create array with value 1  suppose we have array with 8 elements then we have array with 8 1's in array
# start with first index

# nested loop
# i=1, j=0
# first iteration 0, 1 22>10 and 1 <2 1st index =2

# second iteration 
# i=2, j=0, 1
# 9>10, 9>22  1<1

# third iteration 
# i=3, j= 0,1 , 2
# 33>10, 33>22, 33>9
# lis =1 2 3

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

# Dynamic programming Python implementation of LIS problem

# lis returns length of the longest increasing subsequence in arr of size n


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

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))
