
var person1 = { firstName: 'Jon', lastName: 'Kuperman' };
var person2 = { firstName: 'Kelly', lastName: 'King' };

function say2(greeting) {
  console.log(greeting + ' ' + this.firstName + ' ' + this.lastName);
}
say2.apply(person1, ['Hello']); // Hello Jon Kuperman
say2.apply(person2, ['Hello']); // Hello Kelly King

// example

function log(msg){
console.log(msg); // hello world
}
log('hello world')

// Pass multiple parameters-

function log(){
console.log.apply(console, arguments); // hello world
};
log('hello', 'world');
log('hello', 'world', 'new');



// Add data with all logged messages

function log(){
var args = Array.prototype.slice.call(arguments);
args.unshift('(data)');
console.log.apply(console, args); // (data) hello world
};
log('hello', 'world');
log('hello', 'world', 'nnnnn');

// example
var foo = function() {
  var args = Array.prototype.slice.call(arguments);
  console.log(args[1], args ,'arg');
  }
  console.log(foo(1, 2, 4), 'foo')  // undefined
// node js-basics/apply-method.js 