function twoSum(nums, target) {
  let  h = {};
  let n;
for (const iterator in nums) {
    n = target - nums[iterator];
    
    if (!(n  in h)){
        h[nums[iterator]] = iterator;
    }
    else {
        return [h[n], iterator]   
    }
}
};

// console.log(twoSum([2, 7, 11, 15], 9))



console.log(twoSum([5, 9, 3, 2], 5))

