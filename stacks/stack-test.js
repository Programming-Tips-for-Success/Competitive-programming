// The stack is a collection of items. Its structure is based on the Last in First out structure (LIFO) means here it permits one item at a time: the last item inserted. At ‘Top of the stack’ Items are inserted & deleted. It is a dynamic & constantly changing object. All the data items are put on top of the stack and taken off the top. For stacks use push & pop (add to end, take from the end).
 
// Example-
let stack = [];
  stack.push(1);          
  stack.push(2);          
  let last = stack.pop(); // [1]
  console.log(last);      // 2
  
// Point to remember to unshift() and shift() work in specifically the same way as to push() and pop(), respectively, except that they work on the beginning of the array, not the end.