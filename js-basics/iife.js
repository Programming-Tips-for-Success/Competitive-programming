
(function() {

    var msg = "Hello World";

    console.log(msg);

  })();

  // example:
  var main = function() {

    var loop = (function() {

      for (var x = 0; x < 5; x++) {

        //var x scope is only in var loop not outside function

        console.log(x, "x");

      }

    })();

    // console.log("x can not be accessed outside the block scope x value is :"+x);

  };

  main();


  // example
  void (function iife_void() {

    var msg = function() {

      console.log("New world");

    };

    msg();

  })();

  // example

  var foo = "Hello";

  (function() {

    var bar = " World";

    console.log(foo + bar); // hello world

  })();

  // console.log(foo + bar); // cannot access bar here it will show error


  // example
  var var1 = 10;

  var var2 = 3;

  (function() {

    var var1 = 2;

    var2 = 1;

    console.log(var1 + var2); //2 + 1

  })();

  var2 = var2 + var1;

  console.log(var2); // 10 + 1

