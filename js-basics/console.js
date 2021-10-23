console.log(5 % 1, 5 % 2);
console.error('ff');

// value of k?
let i = 3;
let j = 4;
let k = 1;
for (i = 0; i < 3; i++) {
k += j;
j = j - 1;
}
console.log(k, 'k');  // 10

const a = (function() {
    return parseInt("1.5");
    })()
    // What is the data type of a?
    // Select the best option:
    // function
    // object
    // number
    // string
   console.log(a, typeof a, 'a'); 
   
// node js-basics/console.js 