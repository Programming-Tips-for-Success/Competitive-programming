// value assignment & declaration

// let b, a;
//   function foo() {
// let a = b = 0;
// a++;
// return a;
// }
// foo();
// console.log(typeof a);  // undefined
// console.log(typeof b);  // number

let b, a;
  function foo() {
a = b = 0;
a++;
return a;
}
foo();
console.log(typeof a); // number
console.log(typeof b); // number