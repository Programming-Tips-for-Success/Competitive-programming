// In this, we can use this keyword.

   var Animal =function(species, name) {
      var obj ={};
      obj['species'] =species;
      obj['name'] =name;
      extend (obj, objMethods);
      return obj;
        }

      var extend= function(obj, methods) {
      for (var key in methods) {
      obj[key]=methods [key]
      }
      }
      
      var objMethods={
      makeSound: function() {},
      eat: function(){},
      sleep: function(){}
      }
      
      var tiger=Animal('tiger', 'tigger');
      tiger.eat();
      tiger.makeSound();

      // node js-basics/Object-Instantiation/functional-shared.js

