 function reverse(array) { 
    let other = array.length - 1; 
 for (let i = 0; i <= other/2; i++) { 
 let temp = array[i];
 array[i] = array[other-i]; 
 array[other-i] = temp; 
 } 
 console.log(array)
 } 

let arr = [1, 2, 3, 4, 5, 7, 6];

reverse(arr)

  // node problems-js/reverse_arr.js 
