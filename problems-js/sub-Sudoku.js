"use strict";
/*

You are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is "sub-Sudoku", a game where the player has to position the numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix, returns true if  every row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters, so the matrix can contain any signed integer.

Examples:

[[1, 2, 3],
 [3, 1, 2],
 [2, 3, 1]]         -> True

[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]        -> False

[[1, 1, 1],
 [2, 2, 2],
 [3, 3, 3]]        -> False

[[1000, -1000, 6],
 [   2,     3, 1],
 [   3,     1, 2]] -> False

[[0]]              -> False

[[3, 2, 3, 2],
 [2, 3, 2, 3],
 [3, 2, 3, 2],
 [2, 3, 2, 3]] 	-> False

[[2, 3, 4],
 [3, 4, 2],
 [4, 2, 3]]        -> False

[[-1,-2,-3],
 [-2,-3,-1], 
 [-3,-1,-2]]       -> False

[[1,1,1],
 [1,1,2],
 [1,2,3]]          -> False

[[1]]               -> True

n: The number of rows/columns in the matrix

*/

// TODO --- Write your function, returning the result


// True
const grid1 = [
	[1,2,3],
	[3,1,2],
	[2,3,1]
];
// False
const grid2 = [
	[1,2,3],
	[1,2,3],
	[1,2,3]
];
// False
const grid3 = [
	[1,1,1],
	[2,2,2],
	[3,3,3]
];
// False
const grid4 = [
	[1000,-1000,6],
	[2,3,1],
	[3,1,2]
];
// False
const grid5 = [[0]];
// False
const grid6 = [
	[3, 2, 3, 2],
	[2, 3, 2, 3],
	[3, 2, 3, 2],
	[2, 3, 2, 3]
];
// False
const grid7 = [
	[2,3,4],
	[3,4,2],
	[4,2,3]
];
// False
const grid8 = [
	[-1,-2,-3],
	[-2,-3,-1],
	[-3,-1,-2]
];
// False
const grid9 = [
       [1,1,1],
       [1,1,2],
       [1,2,3]
];
// True
const grid10 = [[1]];

// TODO --- Run the test cases from above through your function, printing the returned results

// for loop n= 3 , newarr, break, continue
// const grid1 = [
// 	[1,2,3],
// 	[3,1,2],
// 	[2,3,1]
// ];
// [[1, 2, 3],
//  [1, 2, 3],
//  [1, 2, 3]]       
// [0][0], 
// [1][0], 
// [2][0]

function range(n){
  let arr = [];
  for(let i =1;i<=n;i++){
    arr.push(i);
  }
  return arr;
}

function stringrange(n){
  let str = '';
  for(let i =1;i<=n;i++){
    str += ',' + i;
  }
  return str;
}

function checkSudoku(grid){
//   let newVal = range(n)
   let newVal = range(grid[0].length);
  let arrLength = grid[0].length;
     let finalOutput = false;

for(let i =0;i<arrLength;i++){
 for(let j=0;j<arrLength;j++){
//    if(grid[i][j] == newVal[i] ){
     
//    }
   let valueCheck = false;
   for(let k=0;k<arrLength;k++){
        if(newVal[k] == grid[i][j]){
     valueCheck = true;
   }
  
     if(valueCheck){
       if(grid[i][j] != grid[j][i]){
         finalOutput = true;
       }
     } else {
       finalOutput = false;
     }
     
   }
   
 } 
}
  return finalOutput;
}

console.log(checkSudoku(grid1))
console.log(checkSudoku(grid2))
console.log(checkSudoku(grid3))
console.log(checkSudoku(grid4))
console.log(checkSudoku(grid5))
console.log(checkSudoku(grid6))
console.log(checkSudoku(grid7))
console.log(checkSudoku(grid8))
console.log(checkSudoku(grid9))
console.log(checkSudoku(grid10))
 

// node Problem-Solving/sub-Sudoku.js