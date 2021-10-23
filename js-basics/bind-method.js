var person1 = { firstName: 'Jon', lastName: 'Kuperman' };
var person2 = { firstName: 'Kelly', lastName: 'King' };

function say3() {
  console.log('Hello ' + this.firstName + ' ' + this.lastName);
}

var sayHelloJon = say3.bind(person1);
var sayHelloKelly = say3.bind(person2);

sayHelloJon(); // Hello Jon Kuperman
sayHelloKelly(); // Hello Kelly King

// example
let People = function(person, age) {
    this.person = person;
    this.age = age;
    this.info = function() {
    console.log(this.person + " is " + this.age + " years old" );
    }
}

let person3 = new People('John', 21);
person3.info();  // logs : John is 21 years old

let separated = person3.info.bind(person3);  separated(); // logs : John is 21 years old


// The bind(person3) statement ensures that "this" always refers to person3 inside the bound method- info()

let newObj = {
    person : "sam",
    age : "22",
  }

  // binding the separated method to a new object
 let newBound = person3.info.bind(newObj);
 newBound(); // logs : sam is 22 years old

//  node js-basics/bind-method.js




