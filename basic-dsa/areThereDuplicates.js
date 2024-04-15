//(Frequency Counter)
function areThereDuplicatesFC() {
  let collection = {}
  for(let val in arguments){
    collection[arguments[val]] = (collection[arguments[val]] || 0) + 1
  }
  for(let key in collection){
    if(collection[key] > 1) return true
  }
  return false;
}
// (Multiple Pointers)
function areThereDuplicatesMP(...args) {
  // Two pointers
  args.sort((a,b) => a > b);
  let start = 0;
  let next = 1;
  while(next < args.length){
    if(args[start] === args[next]){
        return true
    }
    start++
    next++
  }
  return false
}
// One Liner Solution
function areThereDuplicates() {
  return new Set(arguments).size !== arguments.length;
}

function print(x){
console.log(x);

}

print(areThereDuplicates(2,3))
print(areThereDuplicates('casd','casd'))
print(areThereDuplicatesMP('casd','casd'))


// node basic-dsa/areThereDuplicates.js