// Frequency Counter / Multiple Pointer - findPair
// Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n. This function should return true if the pair exists or false if it does not.

findPair([6,1,4,10,2,4], 2) // true
findPair([8,6,2,4,1,0,2,5,13],1) // true
findPair([4,-2,3,10],-6) // true
findPair([6,1,4,10,2,4], 22) // false
findPair([], 0) // false
findPair([5,5], 0) // true
findPair([-4,4], -8) // true
findPair([-4,4], 8) // true
findPair([1,3,4,6],-2) // true
findPair([0,1,3,4,6],-2) // true
// Part 1 - solve this with the following requirements:

// Time Complexity Requirement - O(n)

// Space Complexity Requirement - O(n)

// Part 2 - solve this with the following requirements:

// Time Complexity Requirement - O(n log n)

// Space Complexity Requirement - O(1)

// node basic-dsa/findPair.js
