
// simple arrow function
const add2 = (n) => (n + 10);

console.log(add2(9)); // 19

// example

let foo = ( a = 3, b = 5 ) => {
  console.log( a + b , 'foo sum');
  }
  foo()

// example:
var funcs = [];


for (let i = 0; i < 5; i++) {

	funcs.push( ()=>{

		console.log( i );

	} );

}

funcs[2](); // 2

// example
var x = function (a) { return a; };

      // this can also be written as 

      var x = a => a;


      let add = function (a, b) { return a + b; };
      // this can also be written as 
      let add3 = (a, b) => a + b;

      console.log(add3(1, 2)); // 3


   
// example:
        let SumElements = (arr) => {

        let sum = 0;

        for (let element of arr) {

          sum += element;

        }

        console.log(sum); // 220. 

      }

      SumElements([10, 20, 40, 60, 90]);

const b = [1, 2, 3];

const f = (a, ...b) => a + b;

// Tricky thing in this kind of function

console.log(f(1),...b ,'fb'); // 1

function calculate_discount(price, rate = 0.50) {

        return  price * rate;

      }

      console.log(calculate_discount(1000)); //500

      console.log(calculate_discount(1000, 0.30)) //300

     

 // rewritten as

      let calculate_discount2 = (price, rate = 0.50) => price * rate;

      console.log("Discount Amount: ", calculate_discount2(1000)); //Discount Amount: 500

          // ============================ functions with optional parameters ============================

    
    function disp_details(id, name, mail_id) {

      console.log("ID:", id); //ID:111

      console.log("Name", name); //Name mary

      if (mail_id != undefined)  //this condition declaration is must if parameter is optional

        console.log("Email Id", mail_id); //Email Id mary@xyz.com

    }

    disp_details(111, "mary", "mary@xyz.com");

    var func = function (x, y) { return x * y };

    function product() {

      var result;

      result = func(10, 20);

      console.log("The product : " + result)

    }

    product()

    var func1 = new Function("x", "y", "return x*y;");

    function product1() {

      var result;

      result = func1(10, 20);

      console.log("The product2 : " + result)

    }

    product1()

function sayHello(name) {

      var text = 'Hello ' + name;

      var say = function () { console.log(text); } // Hello Joe

      say();

    }

    sayHello('Joe');

    function sayHello2(name) {

      var text = 'Hello ' + name; // Local variable

      var say = function () { console.log(text); }

      return say;

    }

    var say2 = sayHello2('Bob');

    say2(); // logs "Hello Bob"

      function Sandwich2(bread, topping) {

        this.bread = bread;

        this.topping = topping;

        var typicalNumberOfPickles = 2;

        this.howManyPicklesAreOnMySandwich = function () {

          console.log("there are " + typicalNumberOfPickles + "pickles on your " + topping + " sandwich");

        }

      }

      var hamOnWheat = new Sandwich2('wheat', 'ham');

      hamOnWheat.howManyPicklesAreOnMySandwich()   //"there are 2 pickles on your ham sandwich"

   



      function askForMorePickles(topping) {

        let typicalNumberOfPickles = 2;



        return function addAPickleToThisSandwich() {

          let previousPickles = typicalNumberOfPickles;

          typicalNumberOfPickles += 1;

          console.log("There were " + previousPickles + "pickles on your " + topping + " sandwich. Now there are" + typicalNumberOfPickles + " pickles. That is much better!");

        }

      }

      let morePicklesPlease = askForMorePickles('tempeh');

      morePicklesPlease()

      // "There were 2 pickles on your tempeh sandwich. Now there are 3 pickles. That is much better!" 

      morePicklesPlease()

      // "There were 3 pickles on your tempeh sandwich. Now there are 4 pickles. That is much better!"





      var morePicklesForTempeh = askForMorePickles('tempeh');

      var morePicklesForTurkey = askForMorePickles('turkey');

      morePicklesForTempeh()

      // "There were 2 pickles on your tempeh sandwich. Now there are 3 pickles. That is much better!" 

      morePicklesForTurkey()

      // "There were 2 pickles on your turkey sandwich. Now there are 3 pickles. That is much better!" 

        morePicklesForTurkey()

// There were 3 pickles on your 'turkey'sandwich. Now there are 4pickles. That is much better!

// example
var callStore = todoStore(true);
callStore.add('demo');
callStore.add('demo2');




function todoStore(isAuthenticated) {

    let todos = [];
    function add(todo) {
      let start = Date.now();
      if (isAuthenticated) {
        todos.push(todo);
      } else {
        throw "Not authorized to perform this operation";
      }
      let duration = Date.now() - start;
      console.log("add() duration : " + duration, todos);
    }

    return Object.freeze({
      add
    });

  }

// example
  function sum(x) {

    if (arguments.length == 2) {
    
      return arguments[0] + arguments[1];
    
    } else {
    
      return function(y) { return x + y; };
    
    }
    
    }
    
    console.log(sum(2)(3)); // 5


    //  n number of arguments
    function fun1(...params) {

      console.log(params.length);
  
    }
  
    fun1();
  
    fun1(5);
  
    fun1(5, 6, 7);

    // example

    const functionExpression = function(width, height) {

      return width * height;
    
    };
    
    
    console.log(functionExpression(3, 4));
    
    // Result = 12
    
    
    function functionDeclaration(width,height){
    
    return width * height;
    
    };
    
    
    console.log(functionDeclaration(3,4));
    
    //Result = 12
    
    
    
    function getSuperheroPowers() {
      var powers = [];
      var stoneNumber;
      for(stoneNumber = 0; stoneNumber <= 10; stoneNumber++)
      powers [stoneNumber] = function() { return stoneNumber; };
      return powers;
      }
      var powers = getSuperheroPowers();
      console.log(powers[5](), 'getSuperheroPowers')

      var power = "100";
function getPowerNumber()
{
var power = "10";
function f() {
return power;
}
return f;
}
console.log(getPowerNumber()(), 'getPowerNumber')  // 10

// value of a?
function foobar(obj) {
return {
a: obj.bar,
b: obj.baz
}}
const { a } = foobar({ bar: 27, baz: 41 })
console.log(a, 'a'); // 27


//   node js-basics/functions.js



