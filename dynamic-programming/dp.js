// https://cs.slides.com/colt_steele/dynamic-programming#/35/0/0

// WHERE IS THIS ACTUALLY USED?
// Artificial Intelligence
// Speech Recognition
// Caching
// Image Processing
// Shortest Path Algorithms

// DYNAMIC PROGRAMMING
// "A method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions.

// OVERLAPPING
// SUBPROBLEMS
// A problem is said to have overlapping subproblems if it can be broken down into subproblems which are reused several times

// Every number after the first two is the sum of the two preceding ones"
// FIBONACCI

// mergesort

// OPTIMAL SUBSTRUCTURE
// A problem is said to have optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblem

// ENTER
// DYNAMIC PROGRAMMING
// "Using past knowledge to make solving a future problem easier"

// MEMOIZATION

// Storing the results of expensive function calls and returning the cached result when the same inputs occur again

// normal
function fib(n) {
    if (n <= 0) return 0; 
    if (n <= 2) return 1; 

    return fib(n - 1) + fib(n - 2); 
}

// A MEMO-IZED SOLUTION
function fib(n, memo=[]){
  if(memo[n] !== undefined) return memo[n]
  if(n <= 2) return 1;
  var res = fib(n-1, memo) + fib(n-2, memo);
  memo[n] = res;
  return res;
}
// WE'VE BEEN WORKING

// TOP-DOWN

// BUT THERE IS ANOTHER WAY!

// BOTTOM-UP'

// TABULATION
// Storing the result of a previous result in a "table" (usually an array)

// Usually done using iteration

// Better space complexity can be achieved using tabulation

// TABULATED VERSION
function fib(n){
    if(n <= 2) return 1;
    var fibNums = [0,1,1];
    for(var i = 3; i <= n; i++){
        fibNums[i] = fibNums[i-1] + fibNums[i-2];
    }
    return fibNums[n];
}
// MEMOIZATION
function fib(n, savedFib={}) {
   // base case
   if (n <= 0) { return 0; }
   if (n <= 2) { return 1; }


   if (savedFib[n - 1] === undefined) {
        savedFib[n - 1] = fib(n - 1, savedFib);
   }
   
   if (savedFib[n - 2] === undefined) {
        savedFib[n - 2] = fib(n - 2, savedFib);
   }

   return savedFib[n - 1] + savedFib[n - 2];
}
// TABULATION
function fib(n){
    let arr = [0,1]
    // calculating the fibonacci and storing the values
    for(let i = 2; i <= n; i++){
      arr[i] = arr[i-1] + arr[i-2]
    }
    return arr[n]
}

//  node dynamic-programming/dp.js
