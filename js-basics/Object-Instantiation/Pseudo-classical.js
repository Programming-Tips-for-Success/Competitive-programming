// You can implement this with a new keyword.



var Animal = function (species, name) {
    this.species = species;
    this.name = name;
  }
  Animal.prototype.makeSound = function () { },
    Animal.prototype.eat = function () { },
    Animal.prototype.sleep = function () { }
 
  var tiger = new Animal('tiger', 'tigger');
  tiger.eat();
  tiger.makeSound();
 
 //================  Another example of Pseudo-classical Pattern
    function Robot(name, job) {
      this.name = name;
      this.job = job;
    }
    
    Robot.prototype.introduce = function() {
      console.log("Hi! I'm " + this.name + ". My job is " + this.job + ".");
    };
    
    var bender = new Robot("Bender", "bending");
    bender.introduce();  // Hi! I'm Bender. My job is bending.
    console.log(Object.getPrototypeOf(bender) === Robot.prototype);  // true
    
    var wallE = new Robot("Wall-E", "trash collection");
    wallE.introduce();    // Hi! I'm Wall-E. My job is trash collection.
    console.log(Object.getPrototypeOf(wallE) === Robot.prototype);  // true 

    // Object.getPrototypeOf(new Foobar()) refers to the same object as Foobar.prototype.