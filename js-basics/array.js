const fruits = ['apple', 'orange'];
fruits.length = 0;
fruits[0];
console.log(fruits[0]) // undefined

// print b empty array?
let arr = [1,2,3,4,5];
let b = arr;

// first way -
arr.length = []
console.log(b, 'b1');
// second way-
arr.pop()
arr.pop()
arr.pop()
arr.pop()
arr.pop()
console.log(b, 'b2')

// third way-
arr.splice(0)
console.log(b, 'b3');

// problem:
// const length = 4;
// const numbers = [];
// for (var i = 0; i < length; i++); {  // var keyword makes i available outside for loop. and semicolon is not needed
// numbers.push(i + 1);
// }
// console.log(numbers); // [5]

// corrected solution
const length = 4;
const numbers = [];
for (var i = 0; i < length; i++) { 
numbers.push(i + 1);
}
console.log(numbers); // [ 1, 2, 3, 4 ]

// node js-basics/array.js