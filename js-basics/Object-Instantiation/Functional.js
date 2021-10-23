// Here all properties are private since they are contained within the closure scope. In this, we do not use this or a new keyword to create an instance.

var Animal = function (species, name) {
    var obj = {};
    obj['species'] = species;
    obj['name'] = name;
    obj['makeSound'] = function () {
      // code goes here
    }
    obj['eat'] = function () {
      console.log('hi');
      
      // code goes here
    }
    obj['sleep'] = function () {
      // code goes here
    }
    return obj;
  }
  var tiger = Animal('tiger', 'tigger');
  console.log(tiger)
  tiger.eat();
  tiger.makeSound();

