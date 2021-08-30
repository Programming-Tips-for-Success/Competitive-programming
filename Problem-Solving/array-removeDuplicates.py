
class Solution:
    # needs sorted array,  withoutusing new array
    def removeDuplicates(self, nums):
        arr = []
        for f in (set(nums)):
            arr.append(f)
        return arr 

    def countUniqueNumbersFromDuplicates(self, nums):
        b =0
        for i in range(1, len(nums)):
            if(nums[i]!= nums[b]):
                b = b+1
                nums[b] = nums[i]
        return b +1
        
a = Solution()
arr = [1, 1, 2]
print(a.removeDuplicates(arr))
print(a.countUniqueNumbersFromDuplicates(arr))
