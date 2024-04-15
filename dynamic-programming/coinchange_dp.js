// Write a function called coinChange which accepts two parameters: an array of denominations and a value. The function should return the number of ways you can obtain the value from the given collection of denominations. You can think of this as figuring out the number of ways to make change for a given value from a supply of coins.

// If we wanted the least amount of coins, a dynamic programming solution would be more efficient


const denominations = [1, 5, 10, 25]
 
coinChange(denominations, 1) // 1
coinChange(denominations, 2) // 1
coinChange(denominations, 5) // 2
coinChange(denominations, 10) // 4
coinChange(denominations, 25) // 13
coinChange(denominations, 45) // 39
coinChange(denominations, 100) // 242
coinChange(denominations, 145) // 622
coinChange(denominations, 1451) // 425663
coinChange(denominations, 14511) // 409222339

// try it with greedy algo also
 
//  node dynamic-programming/coinchange_dp.js
