var Animal = function (species, name) {
    var obj = Object.create(objMethods);
    obj.species = species;
    obj.name = name;
    return obj;
   }

   var objMethods = {
    makeSound: function () { },
    eat: function () { },
    sleep: function () { }
   }
  
   var tiger = Animal('tiger', 'tigger');
   tiger.eat();
   tiger.makeSound();
   
   //creates a new object with a specified prototype object. It is used for single inheritance
   let bookPrototype = {
    getFullTitle: function () {
      return this.title + " by " + this.author;
    }
   }
   
   let book = Object.create(bookPrototype);
   book.title = "JavaScript: The Good Parts";
   book.author = "Douglas Crockford";
   book.getFullTitle();//JavaScript: The Good Parts by Douglas Crockford
  