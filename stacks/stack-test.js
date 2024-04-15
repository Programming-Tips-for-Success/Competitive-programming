// A LIFO data structure!
// The last element added to the stack will be the first element removed from the stack

// WHERE STACKS ARE USED
// Managing function invocations
// Undo / Redo
// Routing (the history object) is treated like a stack!


let stack1 = [];
stack1.push(1);          
stack1.push(2);          
let last = stack1.pop(); // [1]
console.log(last, stack1);      // 2 [ 1 ]
  

// node stacks/stack-test.js