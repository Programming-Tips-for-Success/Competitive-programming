const shape = {
  radius: 10,
  diameter() {
    return this.radius * 2;
  },
  perimeter: () => 2 * Math.PI * this.radius,
  // perimeter() {return  2 * Math.PI * this.radius},
};

console.log(shape.diameter()); // 20
console.log(shape.perimeter()); // NaN


for (var i = 0; i < 3; i++) { 
  setTimeout(() => console.log(i), 1);
}

// for(let k1=0; k1<5; k1++) {} console.log(k1); 

 function func() { console.log("User1") } function func() { console.log("User2") } function func() { console.log("User3") } function func() { console.log("User4") } func(); 
 const fnc=(function(a) { delete a; return a; })(7); 
 console.log(fnc) 
 for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 1);
}

var a=5 , b=1

var obj = { a : 10 }

with(obj)

{

console.log(b)

}

  

function print() {
  console.log(this, 'function'); // print() {}
 }
 
 let print2 = () => { 
  console.log(this, 'arrow'); // undefined
 }
 
 print();
 print2();


console.log(foo); // tricky Here foo is still undefined 
var foo = function foo(){ 
 	return 12; 
};



var b = 1;
function outer(){
   	var b = 2
    function inner(){
        b++;
        var b = 3;
        console.log(b)
    }
    inner();
}
outer(); // “3” tricky  What will the following code output and why?

// There are three closures in the example, each with it’s own var b declaration. When a variable is invoked closures will be checked in order from local to global until an instance is found. Since the inner closure has a b variable of its own, that is what will be output.

// Furthermore, due to hoisting the code in inner will be interpreted as follows:

function inner () {
    var b; // b is undefined
    b++; // b is NaN
    b = 3; // b is 3
    console.log(b); // output "3"
}


var trees = ["redwood","bay","cedar","oak","maple"];
delete trees[3];
console.log(trees, trees.length) //  What is trees in JavaScript


function foo(){ 
  return foo; 
}
console.log(new foo() instanceof foo); // false

// reverse a string // goh angasal a m'
let str = "i'm a lasagna hog";
console.log(str.split('').reverse().join('')); 

// node problems-js/tricky.js
