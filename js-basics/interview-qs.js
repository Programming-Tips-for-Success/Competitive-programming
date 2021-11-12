// console.log(counter); // show error
let counter = 1;
// _________________
// console.log(func()); // you can use function after the declaration 
let func = () => {
    return `Hello`;
}

// _________________

var x = 1;
function func2() {
  console.log(x, 'x func2');  // undefined because we have initialize the variable with same name
  var x = 2;
}
func2();


// _________________ 

function func3(params) {
    params = true;
}

var value = false;

func3(value);
console.log(value, 'value func3');  // false
// _________________ 

function func4(params) {
    params.x = true;
}

var object = {
    x: false
};

func4(object);
console.log(object.x, 'func4'); // true

// _________________ 





// todo
function outer() 
{ 
    var arr = []; 
    var i;         
    for (i = 0; i < 4; i++) 
    { 
        // storing anonymus function 
        arr[i] = function () { return i; } 

    } 

    // returning the array. 
    return arr; 
} 

var get_arr = outer(); 

console.log(get_arr[0](), 'get_arr 0');  // 4
console.log(get_arr[1]());  // 4
console.log(get_arr[2]());  // 4
console.log(get_arr[3](), 'get_arr 3');  // 4


// -----------------------

function outer2() {
  let counter = 0; 
  function incrementCounter () {
    counter ++;
    console.log(`counter`, counter);
  }
  return incrementCounter;
}

const aCounter = outer2();
const bCounter = outer2();

aCounter();
aCounter();
aCounter();

bCounter();
aCounter();

// ------------
var greeting = `Hello`;
var name = `John`;

function greet() {
    console.log(this.greeting + ` ` + this.name, 'greet3');
}

greet();

const obj = {
    greeting: `Hi`,
    name: `Chris`
};

greet.call(obj);

// --------

console.log(`script start`);

setTimeout(function() {
  console.log(`setTimeout`);
}, 0);

Promise.resolve().then(function() {
  console.log(`promise1`);
}).then(function() {
  console.log(`promise2`);
});

console.log(`script end`);


// --------













function blockFor300ms() {
     /* blocks js thread for 300ms */

     console.log(`Message from block 300ms`);

}

setTimeout(() => {
     console.log(`Hello`);
}, 0);

/// 100ms
// fetch(`https://twitter.com/will/tweets/1`).then(() => {
//      console.log("Data from twitter")
// });

blockFor300ms();

console.log(`Hai!`);

// node js-basics/interview-qs.js 
