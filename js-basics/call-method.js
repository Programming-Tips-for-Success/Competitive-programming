// problem we have to call another function in different functions

// function F() { 
//   console.log(this)
//   this.doSomething('good'); 
// }
// function doSomething(str)
// {
// console.log(str)
//  }
// F();

// [base class].call([child class],[arguments for base class constructor]);


function F() { 
    this.doSomething('good'); 
  }
    // let obj = { doSomething: function(x) { console.log(x); } }
    let obj = { doSomething: (x)=> { console.log(x); } }

    F.call(obj);  // good

    // example
    function Person(name, age) {
      this.name = name || "";
      this.age = age || "";
    }
    function Student(name, age, school) {
      Person.call(this, name, age);  // Call Person function with this and arguments
      this.school = school || "";
    }
    

    function Teacher(first, last, age, gender, interests, subject) {
      Person.call(this, first, last, age, gender, interests);
      this.subject = subject;
     }
    function UndergraduateStudent(name, age, school, year) {
      Student.call(this, name, age, school);  // Call Student function with this and arguments
      this.year = year || "";
    }
    var peter = new UndergraduateStudent('peter', 21, 'EEE', 1);
    console.log(new Student("John Wick", 50).age, 'student'); // 50
    console.log(peter);     // UndergraduateStudent {name: "peter", age: 21, school: "EEE", year: 1}
    console.log(peter instanceof UndergraduateStudent);  // true
    console.log(peter instanceof Student);               // false
    console.log(peter instanceof Person);                // false
    console.log(peter instanceof Object);                // true
    console.log(peter instanceof Date);                  // false
   
    // example
    function Shape(name, sides, sideLength) {
      this.name = name;
      this.sides = sides;
      this.sideLength = sideLength;
     }
     


     var rectangle = function(len, wid)  
{  
this.type = "rectangle";  
this.len = len;  
this.wid = wid;  
}  

var square = function(len) 
{   
rectangle.call(this, len, len);     
}  
var rectangleObj = new rectangle(2, 3);  
console.log(rectangleObj.len);  
console.log(rectangleObj.wid);  
console.log(rectangleObj.type);  

var squareObj = new square(2);  
console.log(squareObj.len); 
console.log(squareObj.wid); 
console.log(squareObj.type); 

//  example    
var person1 = { firstName: 'Jon', lastName: 'Kuperman' };
var person2 = { firstName: 'Kelly', lastName: 'King' };

function say(greeting) {
  console.log(greeting + ' ' + this.firstName + ' ' + this.lastName);
}

say.call(person1, 'Hello'); // Hello Jon Kuperman
say.call(person2, 'Hello'); // Hello Kelly King

// example
var personn = {
  firstName: "John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  }
}

var myObject = {
  firstName: "Mary",
  lastName: "Doe",
}

personn.fullName.call(myObject);  // Will return "Mary Doe"



// node js-basics/call-method.js