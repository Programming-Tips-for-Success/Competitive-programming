
# From the given list of integers and an integer target, return the indices of two numbers whose total is equivalent to the target

# Given nums = [2, 7, 11, 15], target = 9.

# The output should be [0, 1]. 
# Because nums[0] + nums[1] = 2 + 7 = 9.

# The Brute-force solution:
def twoSum(nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
print(twoSum([2, 7, 11, 15], 9))

# The Dictionary Solution:

def twoSum2(nums, target: int):
        dictionary = {}
        answer = []
        
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})

print(twoSum2([2, 7, 11, 15], 9))


# index usage
fruits = ['apple', 'banana', 'cherry']
d = 'cherry'
if d in fruits:
    print(fruits.index(d))