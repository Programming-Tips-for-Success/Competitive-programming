

class People {
name;
constructor(name) {
 this.name = name;
}
getName() {
 return this.name;
}
setName(name) {
 this.name = name;
}
}

let person = new People("Jon Snow");
console.log(person.getName()); // Jon Snow

person.setName("Dany");
console.log(person.getName()); //Dany
console.log(person) // People {name: "Dany"} __proto__: People

// example
let newVariable = function () {
    this.a = 1;
    this.b = 2;
  }
  let newObject = new newVariable(); // {a: 1, b: 2}
  // add properties in newVariable  function's prototype
  newVariable.prototype.b = 3;
  newVariable.prototype.c = 4;
// Now we can see that the properties that we assign to newVariable we can also use this with newObject variable.
  console.log(newObject.a); // 1
  console.log(newObject.b); // 2
  console.log(newObject.c); // 4
  console.log(newObject.d); // undefined

//   example
// Adding Shared properties to Constructor’s .prototype Property and Define a constructor for Circle objects.


function Circle4(radius) {
    this.radius = radius || 1.0;
    this.getArea = function () { return this.radius * this.radius * Math.PI; };
  }

  var circle1 = new Circle4();
  Circle4.prototype.getCircumference = function () { return 2 * this.radius * Math.PI; };
  Circle4.prototype.color = "green";
//   The new properties are available to all instances, including existing ones   

  console.log(circle1.getCircumference());
   console.log(circle1.color, circle1);

   var circle2 = new Circle4(1.5);
   console.log(circle2.getArea());
   console.log(circle2.getCircumference());
   console.log(circle2.color);

//    example
var doSomething = function(){};
console.log( doSomething.prototype ); // {} __proto__: Object
 
function doSomethingNew(){}
doSomethingNew.prototype.foo = "bar"; // add a property onto the prototype
var doSomeInstancing = new doSomethingNew();
doSomeInstancing.prop = "some value"; // add a property onto the object
console.log( doSomeInstancing ); // prop: "some value"

// example
specified ('hello world') // => 'h e l l o  w o r l d'
function specified (str) {
  return str.split('').join(' ');
}
// place the specified function directly on the String object
String.prototype.specified = function(){
  return this.split('').join(' ');
};
console.log('hello world'.specified ())
 
 // example

 function Person() {

 }
Person.prototype.greeting = function() {
  alert('Hi! I\'m ' + this.name.first + '.');
};
 
console.log(Person.prototype, Person.greeting());

function Teacher() {

}
Teacher.prototype = Object.create(Person.prototype);

Object.defineProperty(Teacher.prototype, 'constructor', {
    value: Teacher,
    enumerable: false, // so that it does not appear in 'for in' loop
    writable: true });

console.log(Teacher.prototype);
Teacher.prototype.greeting = function() {
  let prefix;
 
  if (this.gender === 'male' || this.gender === 'Male' || this.gender === 'm' || this.gender === 'M') {
    prefix = 'Mr.';
  } else if (this.gender === 'female' || this.gender === 'Female' || this.gender === 'f' || this.gender === 'F') {
    prefix = 'Ms.';
  } else {
    prefix = 'Mx.';
  }
 
  console.log('Hello. My name is ' + prefix + ' ' + this.name.last + ', and I teach ' + this.subject + '.');
};

let teacher1 = new Teacher('Dave', 'Griffiths', 31, 'male', ['football', 'cookery'], 'mathematics');
console.log(teacher1.greeting(), 'teacher1')
  

 
 // __proto__: doSomethingNew

// node js-basics/prototype.js 
