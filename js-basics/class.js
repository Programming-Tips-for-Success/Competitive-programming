// js class



function Car( model ) {
 
    this.model = model;
    this.color = "silver";
    this.year = "2012";
   
    this.getInfo = function () {
      return this.model + " " + this.year;
    };
   
   }
   
   var myCar = new Car("ford");
    
   myCar.year = "2010";
    
   console.log( myCar.getInfo() ); // ford 2010

   // example
   function Person(name) {

    this.name = name;
    
    this.greeting = function() {
    
      console.log('Hi! I\'m ' + this.name + '.');
    
    };
    
    }
    
    // we can create object using functions
    
    let person1 = new Person('Bob');
    
    let person2 = new Person('Sarah');
    
    
    
    // From Person class, we can now create some actual people: student, teacher
    


class Number2{
  a;
  b;
  c;
  constructor(a, b, c) {
  this.a = a;
  this.b = b;
  this.c = c;
  }
  
  compare(){
  
  console.log(this.a<this.b<this.c, 'less'); // true
  
  console.log(this.c>this.b>this.a, 'greater'); // false
  
  }
  
  }
  
  const j1 = new Number2(5,6,7);
  j1.compare();


  
   // node js-basics/class.js   
