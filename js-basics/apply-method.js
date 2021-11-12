
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



  var obj1 = {
    prop1: 'a',
      valueOfThis: function(){
        console.log(this, 'this1');

        return this.prop1;
      }
    }
   var prop3;
    
   // you cannot use arrow function with objects- try to avoid that- you mannot do that
   var _this = this;
    var obj2 = {
    prop2: 'b',
      valueOfThis: ()=>{
        console.log(this, 'this2');
        return this.prop2;
      }
    }

    console.log(obj1.valueOfThis(), 'function');
    console.log(obj2.valueOfThis(), 'arrow');


// node js-basics/apply-method.js 