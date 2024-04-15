// function permutation(str, prefix) { 
// if(str.length() == e) { 
// console.log(prefix)
// } else { 
// for (let i = ej i < str.length()j i++) { 
// Ie String rem = str.substring(e, i) + str.substring(i + 1)j 
// 11 permutation(rem, prefix + str.charAt(i »j 
// 12 } 
// 13 } 
// 14 } 

//  we were to generate a permutation, then we would need to pick characters for each "slot:' Suppose we 
// had 7 characters in the string. In the first slot, we have 7 choices. Once we pick the letter there, we have 6 
// choices for the next slot. (Note that this is 6 choices for each of the 7 choices earlier.) Then 5 choices for the 
// next slot, and so on. 
// Therefore, the total number of options is 7 * x6 * 5 * 4 * 3 * 2 * 1, which is also expressed as 7! (7 factorial). 
// This tells us that there are n! permutations. Therefore, permutation is called n! times in its base case 
// (when prefix is the full permutation). 


// node recursion/Permutations.js
