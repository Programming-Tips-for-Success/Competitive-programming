// Write a function called stairs which accepts n number of stairs. Imagine that a person is standing at the bottom of the stairs and wants to reach the top and the person can climb either 1 stair or 2 stairs at a time. Your function should return the number of ways the person can reach the top by only climbing 1 or 2 stairs at a time.

function stairs(n) {
  if (n <= 0) return 0;
  if (n <= 2) return n;
  return stairs(n - 1) + stairs(n - 2);
}

// MEMOIZATION SOLUTION
function stairs(n, memo=[]) {
  if (n <= 0) return 0;
  if (n <= 2) return n;
  if (memo[n] > 0) return memo[n];
  memo[n] = stairs(n - 1, memo) + stairs(n - 2, memo);
  return memo[n];
}
// Time Complexity - O(N)

// TABULATION SOLUTION
function stairs(n) {
  if(n < 3) return n;
  let store = [1,1];
  for(let i = 2; i <= n; i++) {
    let total = store[1] + store[0]
    store[0] = store[1]
    store[1] = total
  }
  return store[1];
}
// Time Complexity - O(N)

// Space Complexity - O(1)


//  node dynamic-programming/stairs_problem_dp.js
